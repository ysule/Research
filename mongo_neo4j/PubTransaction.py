
'''MongoDB Connection and Neo4j Transaction Class import'''
import sys
import ast
from socket import *
from pymongo import MongoClient
from py2neo import *
import time
#import neo4jWrapperTransaction as nj
client = MongoClient("localhost",maxPoolSize=None)
db = client['test']
graph = Graph()


'''Node and label Names with Mongo Keys'''

masterNodeType = 'pubid'
masterUniqueName = 'pmid'

nodeTypeIntervention = 'intervention'
uniqueNameInter = 'interventionName'
keyNameIntervention = 'intervention_search_tag'

nodeTypeIndication = 'indication'
uniqueNameIndication = 'indicationName'
keyNameIndication = 'oncology_indication'

nodeTypeMOA = 'moa'
uniqueNameMOA = 'moaName'
keyNameMOA = 'target_tag'

nodeTypeAffiliation = 'affiliations'
uniqueNameAffiliation = 'affiliationName'
keyNameAffiliation = 'affiliations'

nodeTypeAuthor = 'author'
uniqueNameAuthor = 'authorName'
keyNameAuthor = 'author_names'


'''Relation names'''
masterNodeRelation = 'INFORMS_ABOUT'
relationNameMOA = 'FUNCTIONS_AS'
relationNameIndication = 'TREATMENT_FOR'
relationNameAffiliation = 'AFFILIATED_TO'
relationNameAuthor = 'AUTHOR_OF'

t1 = time.time()
f = open('times.txt','a')
f.write('--------------------------------------------------\n')
'''Make Mongo Cursor'''
def mongoQuery() :
    count = 0
    cursor = db.publicationsNeo.find(no_cursor_timeout=True).batch_size(500)
    for record in cursor :
        print(count,':',record['pmid'])
        if count%1000 == 0:
            print time.time() - t1
            f.write(str(count)+'    '+str(time.time() - t1)+'\n')
            f.flush()
        processRecords(record)
        count += 1


'''Process Records'''
def processRecords(record) :
    if 'pmid' in record :
        pmid  = record['pmid']
    else :
        pmid = ''

    # makePMIDNode(record)

    makeInterventionNode(record)

 	# makeAuthorNode(record,listofDicts)

#     makeGeneNode(record)

#     makeBiomarkerNode(record)


def makePMIDNode(record) :
    #tx =graph.begin()
    t = 1
    # attDict = {'journal_title':record['journal_title'], 'abstract':record['abstract']}
    dictOfPMID = {'nodeLabel':masterNodeType,'nodeType':masterUniqueName,'pmid':record['pmid']}
    # dictOfPMID.update(attDict)
    createNode(list(dictOfPMID),t)

def makeInterventionNode(record) :
    #tx =graph.begin()
    t = 0
    if keyNameIntervention in record :
        intervention = list(set(record[keyNameIntervention]))
        interventionList = [{'nodeLabel':nodeTypeIntervention,'nodeType':uniqueNameInter,'nodeValue':entry} for entry in intervention]
        createNode(interventionList,t)
        makeAuthorNode(record,interventionList)
        interventionList = []
    else :
        pass


def makeMOANode(record) :
    #tx =graph.begin()
    t = 0
    if keyNameMOA in record :
        moas = list(set(record[keyNameMOA]))
        moaList = [{'nodeLabel':nodeTypeMOA,'nodeType':uniqueNameMOA,'nodeValue':entry} for entry in moas]
        createNode(moaList,t)
        moaList = []
    else :
        pass


def makeIndicationNode(record):
    #tx=graph.begin()
    t = 0
    if keyNameIndication in record :
        indications = list(set(record[keyNameIndication]))
        indicationList = [{'nodeLabel':nodeTypeIndication,'nodeType':uniqueNameIndication,'nodeValue':entry} for entry in indications]
        createNode(indicationList,t)
        indicationList = []
    else :
        pass


def makeAuthorNode(record,listofDicts) :
    tx=graph.begin()
    t = 0
    if keyNameAuthor in record :
    	relationName = 'knows_About'
    	authors = record['author_names']
    	authorList = [{'nodeLabel':nodeTypeAuthor,'nodeType':uniqueNameAuthor,'nodeValue':entry} for entry in authors]
    	createNode(authorList,t)
    	createRelation(authorList,listofDicts,relationName,tx)
    	authorList = []
    else :
    	pass


def makeAffiliationNode(record) :
    #tx =graph.begin()
    t = 0
    if keyNameAffiliation in record :
        affiliations = list(set(record[keyNameAffiliation]))
        affList = [{'nodeLabel':nodeTypeAffiliation,'nodeType':uniqueNameAffiliation,'nodeValue':entry} for entry in affiliations]
        createNode(affList,t)
        affList = []
    else :
        pass






def createNode(listNodeNames,transactionVar) :
    #tx = transactionVar
    # for inner_dict in listNodeNames :
    #     print(inner_dict)
    #     if 'pmid' in inner_dict.keys() :
    #         statement = 'MERGE(n:'+entry['nodeLabel']+'{'+entry['nodeType']+':"'+entry['nodeValue']+'title:'+entry['journal_title']+'abstract:'+entry['abstract']+'})'
    #         tx.run(statement)

    #     else :
    #for entry in listNodeNames :
    #    statement = 'MERGE(n:'+entry['nodeLabel'].encode('utf-8')+'{'+entry['nodeType'].encode('utf-8')+':"'+str(entry['nodeValue'].encode('utf-8'))+'"})'
    #    tx.run(statement)
    a = 1

'''Method to create relationships between nodes'''
list_s3 = list('')
list_s2 = list('')
list_s1 = list('')
def createRelation(listofDict1,listofDict2,relationName,transactionVar) :
    rel = relationName
    tx = transactionVar
    for entry in listofDict1 :
        statement3 = 'CREATE(n:'+entry['nodeLabel'].encode('utf-8')+'{'+entry['nodeType'].encode('utf-8')+':"'+str(entry['nodeValue'].encode('utf-8'))+'"})'
        if statement3 in list_s3:
            pass
        else:
            list_s3.append(statement3)
            tx.run(statement3)
        for entry1 in listofDict2 :
            statement2 = 'CREATE(n:'+entry1['nodeLabel'].encode('utf-8')+'{'+entry1['nodeType'].encode('utf-8')+':"'+str(entry1['nodeValue'].encode('utf-8'))+'"})'
            if statement2 in list_s2:
                pass
            else:
                list_s2.append(statement2)
                tx.run(statement2)
            statement1 = 'MATCH (u1:'+entry['nodeLabel'].encode('utf-8')+'{'+entry['nodeType'].encode('utf-8')+':"'+entry['nodeValue'].encode('utf-8')+'"}),(u2:'+entry1['nodeLabel'].encode('utf-8')+'{'+entry1['nodeType'].encode('utf-8')+':"'+entry1['nodeValue'].encode('utf-8')+'"}) CREATE(u1)-[:'+relationName+']->(u2)'
            if statement1 in list_s1:
                pass
            else:
                list_s1.append(statement1)
                tx.run(statement1)
    tx.commit()







if __name__ == '__main__' :
#     setupDB()
    mongoQuery()
