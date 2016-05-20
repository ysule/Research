#AUTHOR: Pradumna Panditrao
#Modified by Bedapudi Praneeth
from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
import time

start_time = time.time()

client = MongoClient('localhost',27017)

#Change to your own DB
db = client.dummy20

#2.3 is the one below
#es = Elasticsearch(['http://admin:bedapudi@cd2439091800c988ed9bcbe0640cd795.us-east-1.aws.found.io:9200/'])
#1.7 is the one below
es = Elasticsearch(['http://admin:bedapudi@2266fefcd42109a93821ac9f578b98dd.us-east-1.aws.found.io:9200/'])
#2.3 on localhost is below
es = Elasticsearch(['http://127.0.0.1:9200/'])
#1.7 on localhost is below
es = Elasticsearch(['http://127.0.0.1:6788/'])



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