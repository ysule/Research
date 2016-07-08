import os
import pymongo
from pymongo import MongoClient
import ast

client = MongoClient()
db = client.test
#getting the names of all pdf files in the current folder
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files = filter(lambda f: f.endswith(('.pdf')), files)
for pdf_file in files:
    try:
        #checking and creating text file for pdf file if text file is not there
        text_files = [f for f in os.listdir('.') if os.path.isfile(f)]
        text_files = filter(lambda f: f.endswith(('.html')), text_files)
        text_file = pdf_file.replace('.pdf','') + '.html'
        if text_file not in text_files:
            os.system("pdf2txt.py -o " + pdf_file.replace('.pdf','') + '.html -t html '+pdf_file)
    except:
        print pdf_file.replace('.pdf','') + '.html' + 'could not be converted into text format'
