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
	if 'investigators' in result_object:
		i=0
		while i<len(result_object['investigators']):
			head, sep, tail = result_object['investigators'][i]['last_name'].partition(',')
			result_object['investigators'][i]['last_name'] = head
			result_object['investigators'][i]['last_name'] = result_object['investigators'][i]['last_name'].replace("-"," ")
			i = i+1
	db.praneeth_i.insert(result_object)
