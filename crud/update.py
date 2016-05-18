import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from elasticsearch import Elasticsearch

url = raw_input("Enter the url: ")

while True:
	id = raw_input("Enter the id of the object you want to update ")
	data = raw_input("Enter the data in JSON format ")
	curl = 'curl -XPOST "' + url + '/' + id + '/_update"'+' -d ' + "'{" + '"doc":' + data + "}'"
	os.system(curl)
	print 'updated!'