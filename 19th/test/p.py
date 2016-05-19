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

while True:
	old_count = db.oplog.rs.count({'op':'u'})
	print old_count
	sleep(1)
	cursor = db.oplog.rs.find({'op':'u'},{'o':1}).sort("o",pymongo.ASCENDING).limit(2)
	new_count = 0
	for result_object in cursor:
		del result_object['o']['_id']
		print result_object['o']