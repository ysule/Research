import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

url = raw_input("Enter the url: ")
term = raw_input("Enter the term: ")
field = raw_input("Enter the field: ")

url_new = url + '/_search'
print url_new
#function to get data according to url and term
def search(url_new, field, term):
    query = json.dumps({"query":{"match":{field:term}}})
    response = requests.get(url_new, data=query)
    results = json.loads(response.text)
    return results

def delete(results):
	data = [doc for doc in results['hits']['hits']]
	for doc in data:
		s = 'curl -XDELETE '+url+'/'+doc['_id']
		os.system(s)
		
delete(search(url_new, field, term))
