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

client = MongoClient()

#DB name and COLLECTION names change below
#db = client.IVF_data

#cursor_lname = db.praneeth_a.find({ 'impact_factor' : { '$exists' : 'true' } })

for result_object in cursor_lname:
	i = 0
	while i<len(result_object['authors']):
		print result_object['authors'][i-1]['author_name']
		count = count+1
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
		#print result_object['authors'][i-1]['score']
		i = i+1
	
