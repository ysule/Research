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

#Finding the intial count of total number of updations and insertions on the database
#old_count_update is the initial count of all update records in oplog.
#ol_count_insert is the initial count of all insert records in oplog
old_count_update = db.oplog.rs.count({'op':'u'})
old_count_insert = db.oplog.rs.count({'op':'i'})

while True:
	#setting new count values to zero
	new_count_update = 0
	new_count_insert = 0
	old_count_insert = 0
	old_count_update = 0
	for_new_count = db.oplog.rs.find({'ns':collection_name})
	for obj in for_new_count:
		try:
			obj['u']
			old_count_update = old_count_update + 1
		except:
			try:
				obj['i']
				old_count_insert = old_count_insert + 1
			except:
				pass
	#sleeping for one second
	#need to think if sleep is necessary at all
	#sleep(1)
	#reading the oplog records into cursor. only the object values are being read ignoring the timestamp etc.
	cursor_update = db.oplog.rs.find({'op':'u'},{'o':1})
	for result_object in cursor_update:
		new_count_update = new_count_update + 1
		if(new_count_update>old_count_update):
			es_id = str(result_object['o']['_id'])
			del result_object['o']['_id']
			data = json.dumps(result_object['o'])
			print data + 'is indexed'
			#response = requests.post(url+es_id, data=data)
	old_count_update = new_count_update

	cursor_insert = db.oplog.rs.find({'op':'i'},{'o':1})
	for result_object in cursor_insert:
		new_count_insert = new_count_insert + 1
		if(new_count_insert>old_count_insert):
			es_id = str(result_object['o']['_id'])
			del result_object['o']['_id']
			data = json.dumps(result_object['o'])
			print data + 'is indexed'
			#response = requests.post(url+es_id, data=data)
	old_count_insert = new_count_insert
