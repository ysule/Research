#3.31939101219 to 1.7 for 1000 records
#50.8462313897 to 2.3 for 1000 records
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

start_time = time.time()

client = MongoClient()

db = client.dummy
collection = db['dummy']
'''
no_records = db.movies.count({})
print 'There are '
print no_records
print ' records in this database'
'''
cursor = db.dummy.find({},{'_id':0})
i = 0
for result_object in cursor:
	i = i+1
	print i
	data = json.dumps(result_object)
	#print data
	#another optionprint tornado.escape.json_encode(result_object)
	url = "http://127.0.0.1:6788/dummy/dummy"
	#data = urllib.urlencode(result_object)
	print data
	response = requests.post(url, data=data)
	#print response
print 'done!'

elapsed_time = time.time() - start_time

print 'time taken is (in seconds)'
print elapsed_time
