from neo4j.v1 import GraphDatabase, basic_auth
import json
import ast
import requests
#Add neo4j's username and password here (if needed)
driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "password"))
session = driver.session()
#This is the index and type to which data is getting indexed
url = "http://127.0.0.1:9200/dummy/dummy"
#Query to get all data from neo4j
result = session.run("MATCH (p) RETURN properties(p)")
for i in result:
    i = str(i)
    i = i.split("=",1)[1]
    i = i[:-1]
    i = i.replace("u'",'"')
    i = i.replace("'",'"')
    i = ast.literal_eval(i)
    try:
        del i['_id']
    except:
        i = i
    i = json.dumps(i)
    response = requests.post(url, data=i)
    print response
