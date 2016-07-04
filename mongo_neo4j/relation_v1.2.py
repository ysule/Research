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

'''Make Mongo Cursor'''
def mongoQuery() :
    cursor = db.publicationsNeo.find(no_cursor_timeout=True).batch_size(500)
    for record in cursor :
        processRecords(record)



'''Process Records'''
def processRecords(record) :
    pmid = record['pmid']
    makePMIDNode(record)


def makePMIDNode(record) :
    dictOfPMID = [{'nodeLabel':masterNodeType,'nodeType':masterUniqueName,'nodeValue':record['pmid']}]
    makeInterventionNode(record,dictOfPMID)
    makeAuthorNode(record,dictOfPMID)

def makeInterventionNode(record,listofDict) :
   if keyNameIntervention in record :
        intervention = record['intervention_search_tag']
        interventionList = [{'nodeLabel':nodeTypeIntervention,'nodeType':uniqueNameInter,'nodeValue':entry} for entry in intervention]
        makeIndicationNode(record,interventionList)
        makeMOANode(record,interventionList)
        interventionList = []
   else :
        pass

def makeAuthorNode(record,listofDicts) :
    if keyNameAuthor in record :
        relationName = 'knows_About'
        authors = record['author_names']
        authorList = [{'nodeLabel':nodeTypeAuthor,'nodeType':uniqueNameAuthor,'nodeValue':entry} for entry in authors]
        createRelation(authorList,listofDicts,relationName)
        makeAffiliationNode(record,authorList)
        authorList = []
    else :
        pass

def makeMOANode(record,listofDicts) :
    if keyNameMOA in record :
        moas = record['target_tag']
        moaList = [{'nodeLabel':nodeTypeMOA,'nodeType':uniqueNameMOA,'nodeValue':entry} for entry in moas]
        createRelation(listofDicts,moaList,relationNameMOA)
        moaList = []
    else :
        pass


def makeIndicationNode(record,listofDicts):
    if keyNameIndication in record :
        listofPMID = [{'nodeLabel':masterNodeType,'nodeType':masterUniqueName,'nodeValue':record['pmid']}]
        indications = record['oncology_indication']
        indicationList = [{'nodeLabel':nodeTypeIndication,'nodeType':uniqueNameIndication,'nodeValue':entry} for entry in indications]
        indicationList = []
    else :
        pass


def makeAffiliationNode(record,listofDicts) :
    if keyNameAffiliation in record :
        affiliations = record['affiliations']
        affList = [{'nodeLabel':nodeTypeAffiliation,'nodeType':uniqueNameAffiliation,'nodeValue':entry} for entry in affiliations]
        affList = []
    else :
        pass




def createRelation(listofDict1,listofDict2,relationName) :
    id_m = 0
    id_m2 = 0
    global k
    global x_m
    global x_m2
    global x_r
    for entry in listofDict1 :
        statement_m = 'CREATE(n:'+entry['nodeLabel'].encode('utf-8')+'{'+entry['nodeType'].encode('utf-8')+':"'+str(entry['nodeValue'].encode('utf-8'))+'"})'
        try:
            id_m = int(x_m[statement_m])
        except:
            x_m[statement_m] = k + 1
            id_m = int(x_m[statement_m])
            k = k+1
        for entry1 in listofDict2 :
            statement_m2 = 'CREATE(n:'+entry1['nodeLabel'].encode('utf-8')+'{'+entry1['nodeType'].encode('utf-8')+':"'+str(entry1['nodeValue'].encode('utf-8'))+'"})'
            try:
                id_m2 = int(x_m2[statement_m2])
            except:
                x_m2[statement_m2] = k+1
                id_m = int(x_m2[statement_m2])
                k = k+1
            #MATCH (a),(b) WHERE ID(a) = 202594 AND ID(b) = 207120 CREATE(a)-[:knows_About]->(b)
            statement_r = 'MATCH (a), (b) WHERE ID(a) = ' + str(id_m) + ' AND ID(b) = ' + str(id_m2) + ' CREATE(a)-[:'+relationName+']->(b)'
            print statement_r
            #print str(len(x_m)) + '     ' + str(len(x_m2)) + '      ' + str(len(x_r))


tx = graph.begin()
a = Node("Person", name="Alice")
tx.create(a)
tx.commit()
tx = graph.begin()
x = tx.run('MATCH (n) RETURN ID(n)')
for i in x:
    k = i[0]
    k = int(k)
tx.commit()
print k
time.sleep(5)


t1 = time.time()
t2 = time.time()
x_m = dict()
x_m_id = 0
x_m2 = dict()
x_m2_id = 0
x_r = dict()
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
    print i
    tx.run(value)
    if i%40 == 0:
        tx.commit()
        tx =graph.begin()
        print '--------------------------'
        print time.time()-t2
        print '--------------------------'
        t2 = time.time()
print 'TOTAL'
print time.time()-t1
