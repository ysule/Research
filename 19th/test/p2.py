#working on the assumption that no records are deleted
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
collection = db['oplog.rs']

old_count = db.oplog.rs.count({'op':'u'})
'''
while True:
	sleep(1)
	new_count = db.oplog.rs.count({'op':'u'})
	#if(new_count>old_count):
		#cursor = db.oplog.rs.find({'op':'u'},{'o':1}).sort("op",pymongo.ASCENDING).limit(new_count-old_count)
	cursor = db.oplog.rs.find({'op':'u'},{'o':1})
	for result_object in cursor:
		del result_object['o']['_id']
		print result_object['o']
'''
cursor1 = db.oplog.rs.find({'op':'i'},{'o':1})
n=0
for result_object in cursor1:
	n = n+1
print n