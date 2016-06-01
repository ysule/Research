#This script calculates score of authors from impact_factor
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

#DB name and COLLECTION names change below
db = client.IVF_data

collection = sys.argv[1]
cursor_lname = db.collection.find()

for result_object in cursor_lname:
	try:
		i = 0
		while i<len(result_object['authors']):
			print result_object['authors'][i-1]['author_name']
			if i==len(result_object['authors'])-1:
				score = result_object['impact_factor']*0.5
				#score = 22
			if i>=10 and i<len(result_object['authors'])-1:
				score = result_object['impact_factor']*0.05
				#score = 23
			if i<len(result_object['authors'])-1 and i<=9:
				score = result_object['impact_factor']/(i+1)
				#score = 24
			result_object['authors'][i-1]['score']=score
			print result_object['authors'][i-1]['score']
			i = i+1
	except KeyError:
		print ' '
	#db.collection.insert(result_object)
