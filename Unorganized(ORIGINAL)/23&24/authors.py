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

cursor_lname = db.ivf_publications.find()

for result_object in cursor_lname:
	if 'authors' in result_object:
		i=0
		while i<len(result_object['authors']):
			head, sep, tail = result_object['authors'][i]['author_name'].partition(',')
			result_object['authors'][i]['author_name'] = head
			result_object['authors'][i]['author_name'] = result_object['authors'][i]['author_name'].replace("-"," ")
			i = i+1
	db.praneeth_a.insert(result_object)
