#This script assigns scores to author_names in congresses collections
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from time import sleep
import string
import sys

client = MongoClient()

db = client.IVF_data

collection = sys.argv[1]
cursor_lname = db[collection].find()

for result_object in cursor_lname:
	i = 1
	while i<=len(result_object['author_names']):
		if i==1:
			score = 10
		else:
			score = 8
		result_object['author_scores'][i-1]['score'] = score
		i=i+1
#db.praneeth_congress.remove()
#db.praneeth_congress.insert(result_object)

