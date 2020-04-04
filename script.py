############################
#Author llamasfSpn GitHub
#Datasets from https://github.com/datadista/datasets.git
#Licence GPL
#Instalation necesary: pip install GitPython
############################
import csv
from itertools import izip
import git
import os
from time import sleep

#Functions GIT
def git_clone(url):
    if not os.path.isdir('./datasets'):
        print("GIT START CLONE")
        git.Git("./").clone(url)
        print("GIT END CLONE")

def git_pull():
    print("GIT START PULL")
    g = git.cmd.Git('./datasets')
    g.pull()
    print("GIT END PULL")

#Download Repository
url = "https://github.com/datadista/datasets.git"
git_clone(url)
git_pull()
#create dir output
if not os.path.isdir('./datasets/output'):
    os.mkdir('./datasets/output')



#Function Revert CSV
#Revert row and columns, edit rows
#Treat dataset
def revert_csv(name,inputFileName,outputFileName,outputFileEndName):
    print("Start Revert "+name)
    a = izip(*csv.reader(open(inputFileName, "rb")))
    csv.writer(open(outputFileName, "wb")).writerows(a)
    with open(outputFileName, 'rb') as inFile, open(outputFileEndName, 'wb') as outfile:
        r = csv.reader(inFile)
        w = csv.writer(outfile)
        i=1
        for row in r:
                if i==1:
                    w.writerow(['CCAA','Andalucia','Aragon','Asturias','Baleares','Canarias','Cantabria','Castilla-La Mancha','Castilla y Leon','Cataluna','Ceuta','C. Valenciana','Extremadura','Galicia','Madrid','Melilla','Murcia','Navarra','Pais Vasco','La Rioja'])
                elif i==2:
                    w.writerow(['date','number','number','number','number','number','number','number','number','number','number','number','number','number','number','number','number','number','number','number'])
                else:
                    w.writerow(row[:-1])
                i += 1
    os.remove(outputFileName)
    sleep(2)
    print("End Revert "+name)

#Deaths People Spain
inputFileDeathsName="./datasets/COVID 19/ccaa_covid19_fallecidos.csv"
outputFileDeathsName="./datasets/output/ccaa_covid19_fallecidos_test.csv"
outputFileEndDeathsName="./datasets/output/ccaa_covid19_fallecidos_output.csv"
revert_csv("Deaths CSV",inputFileDeathsName,outputFileDeathsName,outputFileEndDeathsName)
#Infected People Spain
inputFileInfectedName="./datasets/COVID 19/ccaa_covid19_casos.csv"
outputFileInfectedName="./datasets/output/ccaa_covid19_casos_test.csv"
outputFileEndInfectedName="./datasets/output/ccaa_covid19_casos_output.csv"
revert_csv("Infected CSV",inputFileInfectedName,outputFileInfectedName,outputFileEndInfectedName)


#Function Get Total
#Treat dataset
def get_total(name,inputFileName,outputFileName):
    print("Start Total "+name)
    with open(inputFileName, 'rb') as inFile, open(outputFileName, 'wb') as outfile:
        r = csv.reader(inFile)        
        w = csv.writer(outfile)        
        i=1
        for row in r:
                lines = []
                if i==1:
                    w.writerow(['CCAA','Total'])
                else:
                    lines.append(row[1])
                    lines.append(row[-1])
                    w.writerow(lines)
                i += 1
    sleep(2)
    print("End Total "+name)

#Deaths People Total Spain
outputFileDeathsTotalName="./datasets/output/ccaa_covid19_fallecidos_total_output.csv"
get_total("Deaths CSV",inputFileDeathsName,outputFileDeathsTotalName)
#Infected People Spain
outputFileInfectedTotalName="./datasets/output/ccaa_covid19_casos_total_output.csv"
get_total("Infected CSV",inputFileInfectedName,outputFileInfectedTotalName)