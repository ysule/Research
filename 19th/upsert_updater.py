import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

client = MongoClient()

db = client.local
collection = db['oplog.rs']