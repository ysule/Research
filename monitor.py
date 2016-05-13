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
collection = db['rs']

while (1>0):
	n=db.oplog.rs.count()
	sleep(1)
	n_new=db.oplog.rs.count()
	if(n_new>n):
		i=0
		cursor = db.oplog.rs.find({},{"ts:0","t:0","h:0","v:0","op:0"})
		for result_object in cursor:
			data = result_object
			i=i+1
			if(i>n):
				print result_object
			else:
				print 'no updates'
	else:
		print 'no updates'
	
