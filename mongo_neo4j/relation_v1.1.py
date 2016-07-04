
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
'''Make Mongo Cursor'''
def mongoQuery() :
    count = 0
    cursor = db.publicationsNeo.find(no_cursor_timeout=True).batch_size(500)
    for record in cursor :
        processRecords(record)


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
    t = 0
    if keyNameAuthor in record :
    	relationName = 'knows_About'
    	authors = record['author_names']
    	authorList = [{'nodeLabel':nodeTypeAuthor,'nodeType':uniqueNameAuthor,'nodeValue':entry} for entry in authors]
    	createNode(authorList,t)
    	createRelation(authorList,listofDicts,relationName)
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

def createRelation(listofDict1,listofDict2,relationName) :
    global x_m
    global x_m2
    global x_r
    for entry in listofDict1 :
        statement_m = 'CREATE(n:'+entry['nodeLabel'].encode('utf-8')+'{'+entry['nodeType'].encode('utf-8')+':"'+str(entry['nodeValue'].encode('utf-8'))+'"})'
        x_m.add(statement_m)
        for entry1 in listofDict2 :
            statement_m2 = 'CREATE(n:'+entry1['nodeLabel'].encode('utf-8')+'{'+entry1['nodeType'].encode('utf-8')+':"'+str(entry1['nodeValue'].encode('utf-8'))+'"})'
            # #statement_r = MATCH (u1:'+entry['nodeLabel'].encode('utf-8')+'{'+entry['nodeType'].encode('utf-8')+':"'+entry['nodeValue'].encode('utf-8')+'"}),(u2:'+entry1['nodeLabel'].encode('utf-8')+'{'+entry1['nodeType'].encode('utf-8')+':"'+entry1['nodeValue'].encode('utf-8')'"}) CREATE(u1)-[:'+relationName+']->(u2)'
            # statement_r = 'MATCH (u1:'+entry['nodeLabel'].encode('utf-8')+'),(u2:'+entry1['nodeLabel'].encode('utf-8')+')CREATE(u1)-[:'+relationName+']->(u2)'
            statement_r = 'MATCH (u1:'+entry['nodeLabel']+'{'+entry['nodeType']+':"'+entry['nodeValue']+'"}),(u2:'+entry1['nodeLabel']+'{'+entry1['nodeType']+':"'+entry1['nodeValue']+'"}) CREATE(u1)-[:'+relationName+']->(u2)'
            x_m2.add(statement_m2)
            x_r.add(statement_r)
            print str(len(x_m)) + '     ' + str(len(x_m2)) + '      ' + str(len(x_r))


t1 = time.time()
t2 = time.time()
x_m = set()
x_m2 = set()
x_r = set()
mongoQuery()
tx =graph.begin()
for i,value in enumerate(x_m):
    print i
    tx.run(value)
    if i%2000 == 0:
        tx.commit()
        tx =graph.begin()
        print '--------------------------'
        print time.time()-t2
        print '--------------------------'
        t2 = time.time()
tx.commit()

tx =graph.begin()
for i,value in enumerate(x_m2):
    print i
    tx.run(value)
    if i%2000 == 0:
        tx.commit()
        tx =graph.begin()
        print '--------------------------'
        print time.time()-t2
        print '--------------------------'
        t2 = time.time()
tx.commit()

tx =graph.begin()
for i,value in enumerate(x_r):
    print value
    # print i
    # tx.run(value)
    # if i%40 == 0:
    #     tx.commit()
    #     tx =graph.begin()
    #     print '--------------------------'
    #     print time.time()-t2
    #     print '--------------------------'
    #     t2 = time.time()
print 'TOTAL'
print time.time()-t1
