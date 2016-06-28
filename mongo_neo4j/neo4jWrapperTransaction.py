
'''libraries and Authentication'''
from py2neo import *
import sys

# authenticate("localhost:7474", "neo4j", "kinslayer")
# graphDB = Graph()
# tx = graphDB.begin()


# '''Method to create Uniqueness constraint on nodes and Labels'''
# def setupDB() :
#     graphDB.schema.create_uniqeness_constraint("pubid", "pmid")
#     graphDB.schema.create_uniqueness_constraint("moa", "target_tag")
#     graphDB.schema.create_uniqeness_constraint("indication", "oncology_indication")
#     graphDB.schema.create_uniqeness_constraint("intervention", "intervention_search_tag")
#     graphDB.schema.create_uniqeness_constraint("affiliation", "affiliations")
#     graphDB.schema.create_uniqeness_constraint("author", "author_names")



'''list of Dictionaries containing the values of label, nodeType and its value'''

def createNode(listNodeNames,transactionVar) :
    tx = transactionVar
    # for inner_dict in listNodeNames :
    #     print(inner_dict)
    #     if 'pmid' in inner_dict.keys() :
    #         statement = 'MERGE(n:'+entry['nodeLabel']+'{'+entry['nodeType']+':"'+entry['nodeValue']+'title:'+entry['journal_title']+'abstract:'+entry['abstract']+'})'
    #         tx.run(statement)
        
    #     else :
    for entry in listNodeNames :
        statement = 'MERGE(n:'+entry['nodeLabel']+'{'+entry['nodeType']+':"'+str(entry['nodeValue'])+'"})'
        tx.run(statement)


'''Method to create relationships between nodes'''
def createRelation(listofDict1,listofDict2,relationName,transactionVar) :
    rel = relationName
    tx = transactionVar
    for entry in listofDict1 :
        for entry1 in listofDict2 :

            statement1 = 'MATCH (u1:'+entry['nodeLabel']+'{'+entry['nodeType']+':"'+entry['nodeValue']+'"}),(u2:'+entry1['nodeLabel']+'{'+entry1['nodeType']+':"'+entry1['nodeValue']+'"}) MERGE(u1)-[:'+relationName+']->(u2)'
            
            tx.run(statement1)
    tx.commit()