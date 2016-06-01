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

cursor_lname = db.praneeth.find()
db.praneeth_phase.remove({})
for result_object in cursor_lname:
	if('sponsors' in result_object):
		i = 0
		while i < len(result_object['sponsors']):
			if "Merck sharp" in result_object['sponsors'][i]['sponsor']:
				print result_object['sponsors'][i]['sponsor']
				print 'is changed to'
				result_object['sponsors'][i]['sponsor'] = 'MSD'
				print result_object['sponsors'][i]['sponsor']
			else:
				print 'not changed'
			i = i+1
	#db.collection.insert(result_object)
