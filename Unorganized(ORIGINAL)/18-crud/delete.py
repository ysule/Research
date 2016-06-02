import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

print 'if you want to delete by id enter 1'
print 'if you want to delete by key words i.e:all matching items enter 2'

a = int(input("Enter your option: "))

if a==2:
	url = raw_input("Enter the url: ")
	field = raw_input("Enter the field: ")
	term = raw_input("Enter the term: ")

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
if a==1:
	url = raw_input("Enter the url: ")
	id = raw_input("Enter id: ")
	s = 'curl -XDELETE '+url+'/'+  id
	os.system(s)