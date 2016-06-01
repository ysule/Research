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
	if('phase' in result_object):
		if result_object['phase'] =='Phase 4':
			result_object['phase'] ='Phase IV'
		if result_object['phase'] =='Phase 3':
                        result_object['phase'] ='Phase III'
		if result_object['phase'] =='Phase 2':
                        result_object['phase'] ='Phase II'
		if result_object['phase'] =='Phase 1':
                        result_object['phase'] ='Phase I'
		#print result_object['phase']
	db.praneeth_phase.insert(result_object)
