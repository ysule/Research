#working on the assumption that no records are deleted
#This script scans for any new additions(insertions) to the MongoDB database "dummy" (collection is dummy4) and indexes only the newly inserted #documents
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from time import sleep

client = MongoClient()
#conencting to database named dummy
db = client.dummy

while (1>0):
	#counting the number of documents in database and pausing for one second.
	old_count = db.dummy4.count()
	#print old_count
	sleep(1)
	cursor = db.dummy4.find({},{'_id':0})
	new_count=0
	for result_object in cursor:
		new_count = new_count+1
		#print new_count
	#checking if the documnet in result_object is new or old
		if(new_count>old_count):
			#print 1
			print new_count
			data = json.dumps(result_object)
			print data
			url = "http://127.0.0.1:9200/dummy/dummy"
			response = requests.post(url, data=data)
