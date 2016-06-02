import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
from elasticsearch import Elasticsearch

url = raw_input("Enter the url: ")

while True:
	data = raw_input("Enter the data in JSON format")
	requests.post(url, data=data)


