from elasticsearch import Elasticsearch
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

start_at = int(raw_input("Enter where you want to start at: (Enter 0 for default)"))
start_time = time.time()
client = MongoClient()

db = client.KTL

client = Elasticsearch(hosts=[':9200'])
'''
mapping = {
    "author_list_intelligence_v2": {
    "date_detection":False,
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

c = 'curl -XPUT "http://localhost:9200/kols_author_list/author_list_intelligence_v2/_mapping" -d ' + "'" +json.dumps(mapping)+"'"
print c
os.system(c)
'''



bulk_body = ''
cursor = db.normalized_author_list.find({},{'_id':0,'Original affiliation name':1,'Normalized affiliation name':1})

for count,result_object in enumerate(cursor):
    if count>=start_at:
        try:
        	bulk_body = bulk_body + '{ "index" : { "_index" : "normalizedaffiliation", "_type" : "micro"} }\n'
        	bulk_body = bulk_body + json.dumps(result_object)+'\n'
        	if (count+1)%1000 == 0:
        		client.bulk(body=bulk_body)
        		print 'sent the' + str(count/1000) + 'th 1000 documents'
        		bulk_body = ''
        except:
            print 'stopped at '+str(count)

#print bulk_body

client.bulk(body=bulk_body)
elapsed_time = time.time() - start_time
print 'time taken is (in seconds)'
print elapsed_time
