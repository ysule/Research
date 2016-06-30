from pymongo import MongoClient
from py2neo import Graph, Node, Relationship
client = MongoClient("localhost",maxPoolSize=None)
db = client.test
g = Graph()
cursor = db.publicationsNeo.find({})
tx = g.begin()
for i,result in enumerate(cursor):
    a = Node("Person", name="alice")
    tx.create(a)
    print i
tx.commit()
