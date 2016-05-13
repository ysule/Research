import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from time import sleep

client = MongoClient()

db = client.local
'''
while (1>0):
	old_i_count=db.oplog.rs.count({"op":"i"})
	sleep(1)
	new_i_count=db.oplog.rs.count({"op":"i"})
	if(new_i_count>=old_i_count):
		x=db.oplog.rs.find().sort({'ts':1});
		print x
'''
