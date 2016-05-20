#AUTHOR: Pradumna Panditrao

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util

client = MongoClient('localhost',27017)

#db = client.oilbird
db = client.KTL

es = Elasticsearch([{'host':'10.0.1.225',"port":"9200"},{"host":'10.0.1.192',"port":"9200"}])
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

#es.indices.create("kols_clinical_trials")
es.indices.put_mapping(index="kols_clinical_trials", doc_type="onco_clinical_trials_v12", body=mapping)

all_data = db.oilbird_clinical_trials_onco_data_unique.find().batch_size(1000)
count = 0
for x in all_data:
    count += 1
    print count,

    del x['_id']
    try:
        doc_sanitized = json.loads(json_util.dumps(x))
        ret_val = es.index(index="kols_clinical_trials",doc_type="onco_clinical_trials_v12",ignore=400,body=doc_sanitized,request_timeout=60)
        if ret_val['created'] != True:
                    print ret_val['created']
#    print ret_val
    except Exception, e:
        print "error...",e
#        print x['_id']
        print ret_val

