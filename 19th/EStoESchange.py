import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from elasticsearch import Elasticsearch

url = raw_input("Enter the url: ")

if not url:
	url = "http://127.0.0.1:9200/cars/transactions"
	print 'detected no input..'
	print ' Assuming default url:' + url

confirmation = 'y'

while confirmation=='y':
	id = raw_input("Enter the id of the object you want to update:  ")
	data = raw_input("Enter the data in JSON format:  ")
	curl = 'curl -s -XPOST "' + url + '/' + id + '/_update"'+' -d ' + "'{" + '"doc":' + data + "}'" +' >/dev/null'
	os.system(curl)
	print ' '
	print 'done!'
	print ' '
	print"Here is the new document:"
	s = 'curl -XGET '+url+'/'+  id
	os.system(s)
	print ' '
	confirmation = raw_input("Enter y to update another document:")
