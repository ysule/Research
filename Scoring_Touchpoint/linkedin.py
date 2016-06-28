#likes - 1
#dislikes - -1
#comments - 5
#views - 0.1
#scores = scores divided by max possible score
#scores = scores divided by sum of scores
#
#
#
#
#
import pymongo
from pymongo import MongoClient
import json
client = MongoClient()
db = client.test
f_cursor = db.linkedin.find()
f_data = {}
f_no = {}
f_no['l'] = list('')
f_no['c'] = list('')
f_no['s'] = list('')
for f_i,f_result in enumerate(f_cursor):
    f_data[f_i] = {}
    try:
        f_no['l'].append(1*int(f_result['Like']))
    except:
        f_no['l'].append(0)
    try:
        f_no['c'].append(5*int(f_result['Comment']))
    except:
        f_no['c'].append(0)
    try:
        f_no['s'].append(10*int(f_result['Shares']))
    except:
        f_no['s'].append(0)
    f_data[f_i] = f_result
f_max_score = max(f_no['l'])+max(f_no['s'])+max(f_no['c'])
f_total = 0

for i in range(0,f_i):
    f_data[i]['score'] = float(f_no['s'][i]+f_no['c'][i]+f_no['l'][i])/float(f_max_score)
    f_total = f_total + f_data[i]['score']
db.linkedin_scored.drop()
for i in range(0,f_i):
    #dividing scores by sum of scores
    f_data[i]['score'] = float(f_data[i]['score'])/float(f_total)
    #dividing scores by sum of averages of scores
    db.linkedin_scored.insert(f_data[i])
