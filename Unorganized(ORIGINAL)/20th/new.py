from elasticsearch import Elasticsearch

es_client = Elasticsearch(hosts = [{ "host" : "localhost", "port" : 9200 }])

index_name = "test_index"

if es_client.indices.exists(index_name):
    print("deleting '%s' index..." % (index_name))
    print(es_client.indices.delete(index = index_name, ignore=[400, 404]))

print("creating '%s' index..." % (index_name))
print(es_client.indices.create(index = index_name))

bulk_data = []

for i in range(4):
    bulk_data.append({
        "index": {
            "_index": index_name, 
            "_type": 'doc', 
            "_id": i
        }
    })
    bulk_data.append({ "idx": i })

print("bulk indexing...")
res = es_client.bulk(index=index_name,body=bulk_data,refresh=True)
print(res)

print("results:")
for doc in es_client.search(index=index_name)['hits']['hits']:
    print(doc)