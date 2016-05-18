import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

#function to get data according to url and term
def search(url, field, term):
    query = json.dumps({"query":{"match":{field:term}}})
    response = requests.get(url, data=query)
    results = json.loads(response.text)
    return results

#function to format the data prettily
def format(results):
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s" % (doc['_source']))


url = raw_input("Enter the url: ")
field = raw_input("Enter the field: ")
term = raw_input("Enter the term: ")
url = url + '/_search'

#executing the functions
format(search(url, field, term))