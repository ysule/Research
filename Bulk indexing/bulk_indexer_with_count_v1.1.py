from elasticsearch import Elasticsearch
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
import sys
from sys import getsizeof as size

start_at = int(raw_input("Enter where you want to start at: (Enter 0 for default)"))
bulk_size = int(raw_input("Enter bulk object size: "))
start_time = time.time()
client = MongoClient()

db = client.test1

client = Elasticsearch(hosts=[':9201'])

bulk_body = ''
cursor = db.test1.find({},{'_id':0,'Original affiliation name':1,'Normalized affiliation name':1})
for count,result_object in enumerate(cursor):
    if count>=start_at:
        bulk_body = bulk_body + '{ "index" : { "_index" : "test1", "_type" : "test1"} }\n'
        bulk_body = bulk_body + json.dumps(result_object)+'\n'
        if int(size(bulk_body))> 0:
            print size(bulk_body)
            print bulk_body
            client.bulk(body=bulk_body)
            bulk_body = ''

#print bulk_body

client.bulk(body=bulk_body)
elapsed_time = time.time() - start_time
print 'time taken is (in seconds)'
print elapsed_time
