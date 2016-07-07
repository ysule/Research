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
        text_files = filter(lambda f: f.endswith(('.txt')), text_files)
        text_file = pdf_file.replace('.pdf','') + '.txt'
        if text_file not in text_files:
            os.system("pdf2txt.py -o " + pdf_file.replace('.pdf','') + '.txt -t text '+pdf_file)
    except:
        print pdf_file.replace('.pdf','') + '.txt' + 'could not be converted into text format'
#getting the text files names (in the folder) after generating text files for pdfs
text_files = [f for f in os.listdir('.') if os.path.isfile(f)]
text_files = filter(lambda f: f.endswith(('.txt')), text_files)
#for each text file we are reading all the lines in it and checking if it has "EMA" or "FDA" .. etc to find the name of body
for text_file in text_files:
    with open(text_file) as f:
        lines = f.readlines()
        f.close()
        d = dict()
        d['abstract'] = ''
        d['biography'] = ''
        for i,line in enumerate(lines):
            if len(line.split()) < 2:
                if 'biography' in line.lower():
                    for j,line1 in enumerate(lines):
                        if j>i:
                            if 'http:' not in line1:
                                d['biography'] = d['biography'] + line1
                if 'abstract' in line.lower():
                    for k,line2 in enumerate(lines):
                        if k>i:
                            if 'biography' not in line2.lower():
                                if len(line2.split()) < 4:
                                    pass
                                else:
                                    d['abstract'] = d['abstract'] + line2
                            else:
                                break
        d['title'] = ''
        d['author_details'] = list()
        names = dict()
        data = list()
        for i,line in enumerate(lines):
            if i>10 and i<20:
                if len(line)>4:
                    if ',' not in line:
                        data.append(line)
        d['author_details'] = [{"author_name":data[-1]}]
        for i,p in data:
            if p != len(data)-1:
                d['title'] = d['title'] + p

    d['abstract'] = d['abstract'].rstrip().lstrip()
    d['biography'] = d['biography'].rstrip().lstrip()
    d['abstract'] = d['abstract'].replace('\n',' ')
    d['biography'] = d['biography'].replace('\n',' ')
    db.congresses_3rd_world.insert(d)
