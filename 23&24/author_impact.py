import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from time import sleep
import string

client = MongoClient()

db = client.IVF_data

cursor_lname = db.praneeth_a.find({ 'impact_factor' : { '$exists' : 'true' } })
count = 0
for result_object in cursor_lname:
	count = count+len(result_object['authors'])
	i = 1
	while i<=len(result_object['authors']):
		if 10<len(result_object['authors']):
			if i==len(result_object['authors']):
				print result_object['authors'][i-1]['author_name']
				print result_object['impact_factor']*0.5
			if i>10 and i<len(result_object['authors']):
				print result_object['authors'][i-1]['author_name']
				print result_object['impact_factor']*0.05
			if i<len(result_object['authors']) and i<=10:
				print result_object['authors'][i-1]['author_name']
				print result_object['impact_factor']/i

		i=i+1
print count
