import os
import pymongo
import ast
from pymongo import MongoClient
client = MongoClient()
db = client.KTL
#The function is_empty returns 1 (true) if a string does not contain any of the letters or numbers and returns 0 if the string contains any characters or letters
def is_empty(some_string):
    n = 0
    s = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    for i in s:
        if i in some_string:
            n = n+1
    if n>0:
        return 0
    else:
        return 1
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
        all_lines = f.read()
        f.close()
    body_names = [ "EMA", "FDA", "GOV.UK", "CDSCO", "PMDA" ]
    for name in body_names:
        if name in all_lines:
        #we use this variable body_name later while inserting data into mongodb
            body_name = name
    #we are reading each line in text file into list lines
    with open(text_file) as f:
        lines = f.readlines()
        f.close()
    #we are creating a list x and another list temp and we are adding data between two empty lines into each element of list
    #this means that in the list x there are sub-lists each containing all the lines between two empty lines.
    #each sub-list of x contains a line
    x = list('')
    temp = list('')
    for a in lines:
        if is_empty(a):
            x.append(temp)
            temp = list('')
        else:
            temp.append(a)

    for b in x:
        #Here we are first checking if the sublist b in list x is empty
        if len(b)>0:
            #if it is not empty then we are checking if the first element in b (the first line in b) contains ', '
            #we are checking for ', ' because names contain ', ' eg: Bedapudi Praneeth, B.Tech... like this
            if ', ' in b[0]:
                if len(b)>1:
                #affliation is everything after name i.e: affliation is everything except first line in each b
                    affliation = ''
                    for k,p in enumerate(b):
                        if k>0:
                            affliation = affliation + p
                    #The insert statement is like the following
                    if len(affliation.replace(' ',''))<15:
                        affliation = ''
                    insert_data = '{"authorName":"'+str(b[0].replace('\n','')).split(',',1)[0]+'","affiliation":"'+affliation+'","designation":"","body_name":"'+body_name+'"}'
                    #we are removing '\n' because we don't want it to go to next line
                    insert_data = insert_data.replace('\n',' ')
                    db.reg_bodies.insert(ast.literal_eval(insert_data))
