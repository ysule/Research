#Author: Bedapudi Praneeth
from elasticsearch import Elasticsearch
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

start_time = time.time()

client = MongoClient()

db = client.dummy

client = Elasticsearch(hosts=['localhost:9200'])

bulk_body = ''
cursor = db.dummy.find({},{'_id':0})

for result_object in cursor:
	bulk_body = bulk_body + '{ "index" : { "_index" : "dummy1", "_type" : "dummy1"} }\n'
	bulk_body = bulk_body + json.dumps(result_object)+'\n'

print bulk_body

client.bulk(body=bulk_body)
elapsed_time = time.time() - start_time
print 'time taken is (in seconds)'
print elapsed_time


