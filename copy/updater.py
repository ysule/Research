import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from time import sleep
start_time = time.time()

client = MongoClient()

db = client.local
db1 = client.dummy

n_old=db.oplog.rs.count()

while (1>0):
	n=db.oplog.rs.count()
	sleep(1)
	n_new=db.oplog.rs.count()
	if(n_new>n_old):
		i=0
		cursor = db1.dummy.find()
		for result_object in cursor:
			i = i+1
			if(i>n):
				data = json.dumps(result_object)
				url = "http://127.0.0.1:9200/dummy/dummy"
				response = requests.post(url, data=data)
			else:
				x=3
	else:
		print 'no updates!'
