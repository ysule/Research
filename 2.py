import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

start_time = time.time()

client = MongoClient()

db = client.test1
collection = db['movies']
'''
no_records = db.movies.count({})
print 'There are '
print no_records
print ' records in this database'
'''
cursor = db.movies.find({},{'_id':0})
curl = 'curl -XPUT "http://localhost:9200/movies1/movie/_mapping" -d' + "'" + '{ "movie": {"properties": {"director": {"type": "multi_field","fields": {"director": {"type": "string"},"original": {"type" : "string", "index" : "not_analyzed"}} } }}}' + "'"
os.system('./2.sh')
for result_object in cursor:
        data = json.dumps(result_object)
	#print data
	#another optionprint tornado.escape.json_encode(result_object)
	url = "http://127.0.0.1:9200/movies1/movie"
	#data = urllib.urlencode(result_object)
	print data
	response = requests.post(url, data=data)
	#print response
print 'done!'

elapsed_time = time.time() - start_time

print 'time taken is (in seconds)'
print elapsed_time
