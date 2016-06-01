#This script renames Merc sharp ... in sponsors to MSD
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
cursor_lname = db.collection.find()

for result_object in cursor_lname:
	try:
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
	except KeyError:
		garbage = 0
	except TypeError:
		garbage = 0
	#db.collection.insert(result_object)
