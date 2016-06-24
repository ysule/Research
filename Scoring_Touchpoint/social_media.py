import pymongo
from pymongo import MongoClient
import json
client = MongoClient()
db = client.endocrine
cursor = db.endo_blog_data.find({"source":"facebook"})
no = {}
for i,result in enumerate(cursor):
    no[i] = {}
    try:
        no[i]['l'] = len(result['likes']['data'])
    except:
        no[i]['l'] = 0
    try:
        no[i]['c'] = len(result['comments'])
    except:
        no[i]['c'] = 0
    try:
        no[i]['s'] = int(result['shares']['count'])
    except:
        no[i]['s'] = 0
count = i
max_s = 0
max_l = 0
max_c = 0
for i in range(0,count):
    if no[i]['s']>max_s:
        max_s = no[i]['s']
    if no[i]['c']>max_c:
        max_c = no[i]['c']
    if no[i]['l']>max_l:
        max_l = no[i]['l']
max_score = max_s + max_c + max_l
cursor = db.endo_blog_data.find({"source":"facebook"})
for i,result in enumerate(cursor):
    result['score'] = float(no[i]['s']+no[i]['c']+no[i]['l'])/float(max_score)
    db.a.insert(result)



cursor = db.endo_blog_data.find({"source":{'$exists':0}})
no = {}
for i,result in enumerate(cursor):
    no[i] = {}
    try:
        no[i]['l'] = len(result['likes']['data'])
    except:
        no[i]['l'] = 0
    try:
        no[i]['c'] = len(result['comments'])
    except:
        no[i]['c'] = 0
    try:
        no[i]['s'] = int(result['shares']['count'])
    except:
        no[i]['s'] = 0
count = i
max_s = 0
max_l = 0
max_c = 0
for i in range(0,count):
    if no[i]['s']>max_s:
        max_s = no[i]['s']
    if no[i]['c']>max_c:
        max_c = no[i]['c']
    if no[i]['l']>max_l:
        max_l = no[i]['l']
max_score = max_s + max_c + max_l
cursor = db.endo_blog_data.find({"source":{'$exists':0}})
for i,result in enumerate(cursor):
    result['score'] = float(no[i]['s']+no[i]['c']+no[i]['l'])/float(max_score)
    db.a.insert(result)
