#AUTHOR: Pradumna Panditrao

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
import time

start_time = time.time()

client = MongoClient('localhost',27017)

#db = client.oilbird
db = client.dummy20

#2.3 is the one below
#es = Elasticsearch(['http://admin:bedapudi@cd2439091800c988ed9bcbe0640cd795.us-east-1.aws.found.io:9200/'])
#1.7 is the one below
es = Elasticsearch(['http://admin:bedapudi@2266fefcd42109a93821ac9f578b98dd.us-east-1.aws.found.io:9200/'])
#2.3 on localhost is below
es = Elasticsearch(['http://127.0.0.1:9200/'])


#es = Elasticsearch(['10.0.1.75:9200'])
#es = Elasticsearch([{'host':'52.29.219.46',"port":"9200"},{"host":'52.29.206.78',"port":"9200"}])
'''
# Implementation for full and normal text search
'''
'''
mapping = {
    "pub_trial": {
      "properties": {
        "authors": {
          "type": "nested", 
          "properties": {
            "author_name":  { "type":"multi_field", "fields":{ "name":{ "type":"string", "index":"analyzed" },"raw":{ "type":"string", "index":"not_analyzed" }}},
          }
        }
      }
    }
  }
'''
'''
mapping = {
    "onco_clinical_trials_v12": {
    "date_detection":False,
    "properties": {
        "principal_investigators": {
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
'''
#es.indices.create("kols_clinical_trials")
#es.indices.put_mapping(index="dummy", doc_type="dummy", body=mapping)

all_data = db.dummy.find().batch_size(1000)
count = 0
for x in all_data:
    count = count   + 1
    print count,
    del x['_id']
    try:
        doc_sanitized = json.loads(json_util.dumps(x))
        ret_val = es.index(index="dummy",doc_type="dummy",ignore=400,body=doc_sanitized,request_timeout=60)
        if ret_val['created'] != True:
                    print ret_val['created']
#    print ret_val
    except Exception, e:
        print "error...",e
#        print x['_id']
        print ret_val

elapsed_time = time.time() - start_time
print ' '
print elapsed_time
print ' '