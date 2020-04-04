############################
#Author llamasfSpn GitHub
#Datasets from https://github.com/datadista/datasets.git
#
#Instalation: pip install GitPython
############################
import csv
from itertools import izip
import requests
import git
import os

#Functions GIT
def git_clone(url):
    if not os.path.isdir('./datasets'):
        git.Git("./").clone(url)
        print("GIT CLONE")

def git_pull():
    g = git.cmd.Git('./datasets')
    g.pull()
    print("GIT PULL")

#Download Repository
url = "https://github.com/datadista/datasets.git"
git_clone(url)
git_pull()
#create dir output
os.mkdir('./datasets/output')


#Dead People Spain
#Revert row and columns
a = izip(*csv.reader(open("./datasets/COVID 19/ccaa_covid19_fallecidos.csv", "rb")))
csv.writer(open("./datasets/output/ccaa_covid19_fallecidos_output.csv", "wb")).writerows(a)

