
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

def makeInterventionNode(record) :
    #tx =graph.begin()
    t = 0
    if keyNameIntervention in record :
        intervention = list(set(record[keyNameIntervention]))
        interventionList = [{'nodeLabel':nodeTypeIntervention,'nodeType':uniqueNameInter,'nodeValue':entry} for entry in intervention]
        makeAuthorNode(record,interventionList)
        interventionList = []
    else :
        pass


def makeMOANode(record) :
    #tx =graph.begin()
    if keyNameMOA in record :
        moas = list(set(record[keyNameMOA]))
        moaList = [{'nodeLabel':nodeTypeMOA,'nodeType':uniqueNameMOA,'nodeValue':entry} for entry in moas]
        moaList = []
    else :
        pass


def makeIndicationNode(record):
    #tx=graph.begin()
    if keyNameIndication in record :
        indications = list(set(record[keyNameIndication]))
        indicationList = [{'nodeLabel':nodeTypeIndication,'nodeType':uniqueNameIndication,'nodeValue':entry} for entry in indications]
        indicationList = []
    else :
        pass


def makeAuthorNode(record,listofDicts) :
    if keyNameAuthor in record :
    	relationName = 'knows_About'
    	authors = record['author_names']
    	authorList = [{'nodeLabel':nodeTypeAuthor,'nodeType':uniqueNameAuthor,'nodeValue':entry} for entry in authors]
    	joiner(authorList)
    	authorList = []
    else :
    	pass


def makeAffiliationNode(record) :
    #tx =graph.begin()
    if keyNameAffiliation in record :
        affiliations = list(set(record[keyNameAffiliation]))
        affList = [{'nodeLabel':nodeTypeAffiliation,'nodeType':uniqueNameAffiliation,'nodeValue':entry} for entry in affiliations]
        affList = []
    else :
        pass



def joiner(listofDict1):
    for entry in listofDict1:
        statement = 'CREATE(n:'+entry['nodeLabel'].encode('utf-8')+'{'+entry['nodeType'].encode('utf-8')+':"'+str(entry['nodeValue'].encode('utf-8'))+'"})'
        global x
        x.add(statement)
        print len(x)

t1 = time.time()
t2 = time.time()
x = set()
mongoQuery()
tx =graph.begin()
for i,value in enumerate(x):
    print i
    tx.run(value)
    if i%5000 == 0:
        tx.commit()
        tx =graph.begin()
        print '--------------------------'
        print time.time()-t2
        print '--------------------------'
        t2 = time.time()
tx.commit()
print 'TOTAL'
print time.time()-t1
