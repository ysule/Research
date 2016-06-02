#This script changes 1,2,3,4 in phase names to roman numbers
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

cursor_lname = db.ivf_clinical_trails_12052016.find()

for result_object in cursor_lname:
	try:
		if('phase' in result_object):
			if result_object['phase'] =='Phase 4':
				result_object['phase'] ='Phase IV'
			if result_object['phase'] =='Phase 3':
	                        result_object['phase'] ='Phase III'
			if result_object['phase'] =='Phase 2':
	                        result_object['phase'] ='Phase II'
			if result_object['phase'] =='Phase 1':
	                        result_object['phase'] ='Phase I'
			print result_object['phase']
		#db.praneeth_phase.insert(result_object)
	except KeyError:
		garbage = 0
