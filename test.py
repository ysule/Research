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
#while(1>0):
#	cursor = db.oplog.rs.find()
#	for result_object in cursor:
#		data = result_object
#		print result_object
 #                       #else:
  #                      #        print 'no updates'
while(1>0):
	x=db.oplog.rs.count()
	print x
	sleep(10)
	
