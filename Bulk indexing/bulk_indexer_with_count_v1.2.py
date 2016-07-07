from elasticsearch import Elasticsearch
from bson import json_util, ObjectId
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time
import sys
from sys import getsizeof as size

start_at = int(raw_input("Enter where you want to start at: (Enter 0 for default)"))
bulk_size = int(raw_input("Enter bulk object size: "))
start_time = time.time()
client = MongoClient()

db = client.KTL

client = Elasticsearch(hosts=['10.0.1.170:9200'])
#client.indices.create("kols_onco_publications")

def delete_id(obj, key):
    if key in obj: del obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = delete_id(v, key)
            if item is not None:
                return item


mapping = {
    "onco_publications": {
    "date_detection":False,
    "properties": {
        "authors": {
          "type": "nested"
#          "properties": {
#           "last_name":  { "type":"multi_field", "fields":{ "name":{ "type":"string", "index":"analyzed" },"raw":{ "type":"string", "index":"not_analyzed" }}},
#         }
       }
     },
    "dynamic_templates": [
      {
        "string_fields": {
          "mapping": {
            "type": "string",
            "fields": {
              "raw": {
                "index": "not_analyzed",
                "ignore_above": 256,
                "type": "string"
              }
            }
          },
          "match_mapping_type": "string",
          "match": "*"
        }
      }
    ]
  }
}

c = 'curl -XPUT "http://10.0.1.170:9200/kols_onco_publications/onco_publications/_mapping" -d ' + "'" +json.dumps(mapping)+"'"

print c
os.system(c)



bulk_body = ''
cursor = db.oilbird_updated_publications.find({},{"_id":0})
old_count = 0
for count,result_object in enumerate(cursor):
    delete_id(result_object,'_id')
    if count>=start_at:
        bulk_body = bulk_body + '{ "index" : { "_index" : "kols_onco_publications", "_type" : "onco_publications"} }\n'
#        bulk_body = bulk_body + json.loads(json_util.dumps(result_object))+'\n'
	bulk_body = bulk_body + json.dumps(result_object)+'\n'
#	page_sanitized = json.loads(json_util.dumps(page))
        if size(bulk_body)>1000000*bulk_size:
        	client.bulk(body=bulk_body)
        	print 'sent ' + str(count - old_count) + ' documents' + 'TOTAL: ' + str(count)
        	bulk_body = ''
                old_count = count

#print bulk_body

client.bulk(body=bulk_body)
elapsed_time = time.time() - start_time
print 'time taken is (in seconds)'
print elapsed_time
