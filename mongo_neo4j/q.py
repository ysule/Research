from py2neo import Graph, Node, Relationship
g = Graph()
tx = g.begin()
a = Node("Person", name="Alice")
