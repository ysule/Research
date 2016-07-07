#working on the assumption that no records are deleted
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from time import sleep

url = raw_input("Enter the url: ")
collection_name = raw_input("Enter db name and collection name (db.collection):")

if not url:
	url = "http://127.0.0.1:9200/cars/transactions/"
	print 'detected no input..'
	print ' Assuming default url:' + url


client = MongoClient()

db = client.local
collection = db['oplog.rs']

cursor = collection.find()
for new_count, result in enumerate(cursor):
	if 'ns' in result.keys():
		if result['ns'] == collection_name:
			if result['op'] == 'u' or result['op'] == 'i':
				old_count = new_count

while True:
	cursor = collection.find()
	for new_count, result in enumerate(cursor):
		if 'ns' in result.keys():
			if result['ns'] == collection_name:
				if result['op'] == 'u' or result['op'] == 'i':
					if new_count > old_count:
						es_id = str(result['o']['_id'])
						del result['o']['_id']
						data = json.dumps(result['o'])
						print data + 'is indexed'
						#response = requests.post(url+es_id, data=data)
						old_count = new_count
