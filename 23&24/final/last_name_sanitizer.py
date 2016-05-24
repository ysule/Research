#This script sanitizes the last_name in investigators key i.e: Removes "," and "MD","PhD" etc and removes "-"
#If an error shows up after the script runs, ignore it. It doesn't change anything.
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

#edit the below line to set the database.
db = client.IVF_data

#edit the following line to set the collection name
cursor_lname = db.ivf_clinical_trails_12052016.find()

for result_object in cursor_lname:
	#we are exluding result_objects with no 'investigators' key by using the following if condition
	if 'investigators' in result_object:
		#as each 'investigators' key may have more than one 'last_name' we are writing a loop to iterate over the list and select the last_name
		#here please note that a len(result_object['investigators'] gives use the number of last_name keys in eac investigator key
		i=0
		while i<len(result_object['investigators']):
			try:
				#here head gives use the value before ","
				head, sep, tail = result_object['investigators'][i]['last_name'].partition(',')
				#as in each value of the key 'last_name' after "," there are unnecessary characters, we need the string before ","
				result_object['investigators'][i]['last_name'] = head
				print head
				result_object['investigators'][i]['last_name'] = result_object['investigators'][i]['last_name'].replace("-"," ")
			except KeyError:
				print' '
				
			i = i+1
	#THIS IS IMPORTANT
	#HERE WRITE THE MONGO OPERATION YOU NEED
	#IN THE GIVEN EXAMPLE BELOW the output is being inserted into a collection named "praneeth_i"
	#IF YOU NEED TO UPDATE ORIGINAL TABLE, TAKE A BACKUPa OF IT FIRST AND CHANGE TO FOLLOWING LINE TO update
	db.praneeth_clinical.insert(result_object)
