############################
#Author llamasfSpn GitHub
#Datasets from https://github.com/datadista/datasets.git
#Licence GPL
#Instalation necesary: pip install GitPython
############################
import csv
from itertools import izip
import requests
import git
import os

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


#Dead People Spain
#Revert row and columns, delete first row
#Treat dataset
inputFileName="./datasets/COVID 19/ccaa_covid19_fallecidos.csv"
outputFileName="./datasets/output/ccaa_covid19_fallecidos_test.csv"
outputFileEndName="./datasets/output/ccaa_covid19_fallecidos_output.csv"
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
                w.writerow(['date','string','string','string','string','string','string','string','string','string','string','string','string','string','string','string','string','string','string','string'])
            else:
                w.writerow(row[:-1])
            i += 1
os.remove(outputFileName)