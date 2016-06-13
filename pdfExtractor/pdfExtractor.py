import os
import pymongo
import ast
from pymongo import MongoClient
client = MongoClient()
db = client.dummy
def is_empty(x):
    n = 0
    s = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    for i in s:
        if i in x:
            n = n+1
    if n>0:
        return 0
    else:
        return 1
#getting the names of all pdf files in the current folder
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files = filter(lambda f: f.endswith(('.pdf')), files)
for pdf_file in files:
    #checking and creating text file for pdf file if text file is not there
    text_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    text_files = filter(lambda f: f.endswith(('.txt')), text_files)
    text_file = pdf_file.replace('.pdf','') + '.txt'
    if text_file not in text_files:
        os.system("pdf2txt.py -o " + pdf_file.replace('.pdf','') + '.txt -t text '+pdf_file)
#getting the text files names (in the folder) after generating text files for pdfs
text_files = [f for f in os.listdir('.') if os.path.isfile(f)]
text_files = filter(lambda f: f.endswith(('.txt')), text_files)
for text_file in text_files:
    with open(text_file) as f:
        lines = f.readlines()
        f.close()
    list_empty_lines = 0
    x = list('')
    temp = list('')
    for a in lines:
        if is_empty(a):
            x.append(temp)
            temp = list('')
        else:
            temp.append(a)
    '''
    while 1:
        print x[int(raw_input("aa:"))]
    '''
    for i,b in enumerate(x):
        if len(b)>0:
            if ', ' in b[0]:
                if len(b)>1:
                    affliation = ''
                    for k,p in enumerate(b):
                        if k>0:
                            affliation = affliation + p
                    #print affliation + '==================='
                    insert_data = '{"name":"'+str(b[0].replace('\n',''))+'","affiliation":"'+affliation+'"}'
                    insert_data = insert_data.replace('\n',' ')
                    db.dummy.insert(ast.literal_eval(insert_data))
