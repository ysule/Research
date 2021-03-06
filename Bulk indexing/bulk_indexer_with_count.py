from elasticsearch import Elasticsearch
import pymongo
import os
from pymongo import MongoClient
import json
import requests
import urllib
import time

start_time = time.time()

client = MongoClient()

db = client.KTL

client = Elasticsearch(hosts=[':9200'])

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




bulk_body = ''
cursor = db.normalized_author_list.find({},{'_id':0})
count = 0
for result_object in cursor:
	bulk_body = bulk_body + '{ "index" : { "_index" : "kols_author_list", "_type" : "author_list_intelligence_v2"} }\n'
	bulk_body = bulk_body + json.dumps(result_object)+'\n'
	count = count + 1
	if count%1000 == 0:
		client.bulk(body=bulk_body)
		print 'sent the' + str(count/1000) + 'th 1000 documents'
		bulk_body = ''

#print bulk_body

client.bulk(body=bulk_body)
elapsed_time = time.time() - start_time
print 'time taken is (in seconds)'
print elapsed_time
