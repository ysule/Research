#working on the assumption that no records are deleted
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from elasticsearch import Elasticsearch
from time import sleep
from sys import getsizeof as size

index_doc = raw_input("Enter the index name and doctype index_name/doc_type: ")
collection_name = raw_input("Enter db name and collection name (db.collection):")
bulk_size = int(raw_input("Enter bulk object size: "))

if not index_doc:
	index = 'test'
	doc = 'test'
	print 'detected no input..'
	print ' Assuming default index and doctype:' + index + '/' + doc
else:
	index = index_doc.split('/',1)[0]
	doc = index_doc.split('/',1)[0]


client = MongoClient()

db = client.local
collection = db['oplog.rs']

es_client = Elasticsearch(hosts=['127.0.0.1:9200'])

bulk_body = ''
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
						bulk_body = bulk_body + '{ "index" : { "_index" : "'+index+'", "_type" : "'+doc+'"} }\n'
						bulk_body = bulk_body + json.dumps(result['o'])+'\n'
						print result['o'] + ' is added to bulk_body'
						if size(bulk_body)>1000000*bulk_size:
							es_client.bulk(body=bulk_body)
				        	bulk_body = ''
						#response = requests.post(url+es_id, data=data)
						old_count = new_count
