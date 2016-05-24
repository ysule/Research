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

cursor_lname = db.ivf_patents_12052016.find()

for result_object in cursor_lname:
	if 'inventors' in result_object:
		i=0
		while i<len(result_object['inventors']):
			head, sep, tail = result_object['inventors'][i]['name'].partition(',')
			result_object['inventors'][i]['name'] = head
			result_object['inventors'][i]['name'] = result_object['inventors'][i]['name'].replace("-"," ")
			i = i+1
	db.praneeth_p.insert(result_object)
