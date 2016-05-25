#51.4777419567-(old) for 1000
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
import string

start_time = time.time()

client = MongoClient()

db = client.dummy
'''
no_records = db.movies.count({})
print 'There are '
print no_records
print ' records in this database'
'''

cursor = db.dummy.find({},{'_id':0})
a = '{"na":"pe"}'
for r in cursor:
	a = a+json.dumps(r)
#print a
curl = 'curl -XPOST "http://127.0.0.1:9200/dummy/dummy" -d' +" '"+a+"'"
os.system(curl)
elapsed_time = time.time() - start_time

print 'time taken is (in seconds)'
print elapsed_time
