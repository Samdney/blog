from os import listdir
from os.path import isfile, join

pathpdfs = './content/files/pdf'
PDFSINDIR = [f for f in listdir(pathpdfs) if isfile(join(pathpdfs, f))]

pathbibs = './content/files/bib'
BIBSINDIR = [f for f in listdir(pathbibs) if isfile(join(pathbibs, f))]

pathcites = './content/files/cite'
CITESINDIR = [f for f in listdir(pathcites) if isfile(join(pathcites, f))]
