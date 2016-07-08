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
    os.system('python a.py '+pdf_file)
    print pdf_file
