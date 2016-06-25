#likes -1
#comments -10
#shares -5
#First scores are calculated by above weightages
#Scores are divided by max possible score
#Scores are divided by sum of score
#Avg is calculated
#Above steps are repeated for facebook and youtube
#Scores are divided by sum of averages (of facebook and youtube)
import pymongo
from pymongo import MongoClient
import json
client = MongoClient()
db = client.endocrine
f_cursor = db.endo_blog_data.find({"source":"facebook"})
f_data = {}
f_no = {}
f_no['l'] = list('')
f_no['c'] = list('')
f_no['s'] = list('')
for f_i,f_result in enumerate(f_cursor):
    f_data[f_i] = {}
    try:
        f_no['l'].append(1*len(f_result['likes']['data']))
    except:
        f_no['l'].append(0)
    try:
        f_no['c'].append(5*len(f_result['comments']))
    except:
        f_no['c'].append(0)
    try:
        f_no['s'].append(10*(f_result['shares']['count']))
    except:
        f_no['s'].append(0)
    f_data[f_i] = f_result
f_max_score = max(f_no['l'])+max(f_no['s'])+max(f_no['c'])



y_cursor = db.endo_blog_data.find({"source":{'$exists':0}})
y_data = {}
y_no = {}
y_no['l'] = list('')
y_no['c'] = list('')
y_no['s'] = list('')
for y_i,y_result in enumerate(y_cursor):
    y_data[y_i] = {}
    try:
        y_no['l'].append(1*len(y_result['likes']['data']))
    except:
        y_no['l'].append(0)
    try:
        y_no['c'].append(5*len(y_result['comments']))
    except:
        y_no['c'].append(0)
    try:
        y_no['s'].append(10*(y_result['shares']['count']))
    except:
        y_no['s'].append(0)
    y_data[y_i] = y_result
y_max_score = max(y_no['l'])+max(y_no['s'])+max(y_no['c'])
f_total = 0
for i in range(0,f_i):
    f_data[i]['score'] = float(f_no['s'][i]+f_no['c'][i]+f_no['l'][i])/float(f_max_score)
    f_total = f_total + f_data[i]['score']
f_avg = f_total/f_i

y_total = 0
for i in range(0,y_i):
    y_data[i]['score'] = float(y_no['s'][i]+y_no['c'][i]+y_no['l'][i])/float(y_max_score)
    y_total = y_total + y_data[i]['score']
y_avg = y_total/y_i

total_avg = f_avg + y_avg

db.endo_blog_data.remove({})

for i in range(0,f_i):
    #dividing scores by sum of scores
    f_data[i]['score'] = f_data[i]['score']/f_total
    #dividing scores by sum of averages of scores
    f_data[i]['score'] = f_data[i]['score']/total_avg
    db.endo_blog_data.insert(f_data[i])
for i in range(0,y_i):
    #dividing scores by sum of scores
    y_data[i]['score'] = y_data[i]['score']/y_total
    #dividing scores by sum of averages of scores
    y_data[i]['score'] = y_data[i]['score']/total_avg
    db.endo_blog_data.insert(y_data[i])
