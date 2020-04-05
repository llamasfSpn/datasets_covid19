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
    print("Start "+name)
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
    print("End "+name)

#Deaths People Spain
inputFileDeathsName="./datasets/COVID 19/ccaa_covid19_fallecidos.csv"
outputFileDeathsName="./datasets/output/ccaa_covid19_fallecidos_test.csv"
outputFileEndDeathsName="./datasets/output/ccaa_covid19_fallecidos_output.csv"
revert_csv("Revert Deaths CSV",inputFileDeathsName,outputFileDeathsName,outputFileEndDeathsName)
#Infected People Spain
inputFileInfectedName="./datasets/COVID 19/ccaa_covid19_casos.csv"
outputFileInfectedName="./datasets/output/ccaa_covid19_casos_test.csv"
outputFileEndInfectedName="./datasets/output/ccaa_covid19_casos_output.csv"
revert_csv("Revert Infected CSV",inputFileInfectedName,outputFileInfectedName,outputFileEndInfectedName)


#Function Get Total
#Treat dataset
def get_total(name,inputFileName,outputFileName):
    print("Start "+name)
    with open(inputFileName, 'rb') as inFile, open(outputFileName, 'wb') as outfile:
        r = csv.reader(inFile)        
        w = csv.writer(outfile)        
        i=1
        w.writerow(['CCAA','Totales'])
        for row in r:
                lines = []
                if i==1:
                    w.writerow(['string','number'])
                else:
                    if row[1]!='Total':
                        lines.append(row[1])
                        lines.append(row[-1])
                        w.writerow(lines)
                i += 1
    sleep(2)
    print("End "+name)

#Deaths People Total Spain
outputFileDeathsTotalName="./datasets/output/ccaa_covid19_fallecidos_total_output.csv"
get_total("Total Deaths CSV",inputFileDeathsName,outputFileDeathsTotalName)
#Infected People Spain
outputFileInfectedTotalName="./datasets/output/ccaa_covid19_casos_total_output.csv"
get_total("Total Infected CSV",inputFileInfectedName,outputFileInfectedTotalName)


#Function Get National state
#Treat dataset
def get_national_state(name,inputFileName,outputFileName,outputFileEndName):
    print("Start "+name)
    a = izip(*csv.reader(open(inputFileName, "rb")))
    csv.writer(open(outputFileName, "wb")).writerows(a)
    with open(outputFileName, 'rb') as inFile, open(outputFileEndName, 'wb') as outfile:
        r = csv.reader(inFile)        
        w = csv.writer(outfile)        
        i=1
        w.writerow(['Estado','Total'])
        for row in r:
                if i==1:
                    w.writerow(['string','number'])
                else:
                    lines = []
                    lines.append(row[0])
                    lines.append(row[-1])
                    w.writerow(lines)
                i += 1
    os.remove(outputFileName)
    sleep(2)
    print("End "+name)

#Total state People Spain
inputFileState ="./datasets/COVID 19/nacional_covid19.csv"
outputFileState="./datasets/output/nacional_covid19_output.csv"
outputFileTestState ="./datasets/output/nacional_covid19_test.csv"
get_national_state("Total State CSV",inputFileState,outputFileTestState,outputFileState)


#Function Get National state table
#Treat dataset
def get_national_state_table(name,inputFileName,outputFileName,outputFileEndName):
    print("Start "+name)
    a = izip(*csv.reader(open(inputFileName, "rb")))
    csv.writer(open(outputFileName, "wb")).writerows(a)
    with open(outputFileName, 'rb') as inFile, open(outputFileEndName, 'wb') as outfile:
        r = csv.reader(inFile)        
        w = csv.writer(outfile)        
        i=1
        w.writerow(['Estados','Total','-1 dia','-2 dias','-3 dias','-4 dias','-5 dias','Situacion'])
        for row in r:
                if i==1:
                    w.writerow(['string','number','number','number','number','number','number','string'])
                else:
                    lines = []
                    lines.append(row[0])
                    lines.append(row[-1])
                    lines.append(str(int(row[-1])-int(row[-2])))
                    lines.append(str(int(row[-2])-int(row[-3])))
                    lines.append(str(int(row[-3])-int(row[-4])))
                    lines.append(str(int(row[-4])-int(row[-5])))
                    lines.append(str(int(row[-5])-int(row[-6])))
                    if int(row[-1])-int(row[-2]) > int(row[-2])-int(row[-3]):
                        lines.append('Aumenta')
                    else:
                        lines.append('Disminuye')
                    w.writerow(lines)
                i += 1
    os.remove(outputFileName)
    sleep(2)
    print("End "+name)

#Total state People Spain Table
outputFileStateTable="./datasets/output/nacional_covid19_table_output.csv"
outputFileTestStateTable ="./datasets/output/nacional_covid19_table_test.csv"
get_national_state_table("Total State Table CSV",inputFileState,outputFileTestStateTable,outputFileStateTable)