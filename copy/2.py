import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from time import sleep

client = MongoClient()

db = client.local
db1 = client.dummy

while (1>0):
	n=db.oplog.rs.count()
	sleep(1)
	n_new=db.oplog.rs.count()
	if(n_new>n):
		i=0
		while n_new>0:
			n_new = n_new-1
			i=i+1
			if(i>n):
				cursor = db1.dummy.find({},{'_id':0})
				for result_object in cursor:
					
					data = json.dumps(result_object)
					print data
					url = "http://127.0.0.1:9200/update_dummy/dummy"
					response = requests.post(url, data=data)
			else:
				print 'no updates'
	else:
		print 'no updates'
	