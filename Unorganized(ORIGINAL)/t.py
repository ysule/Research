# Adapted from the example here: https://jira.mongodb.org/browse/PYTHON-735
# to work with pymongo 3.0

import pymongo
from pymongo.cursor import CursorType

c = pymongo.MongoClient()

# Uncomment this for master/slave.
oplog = c.local.oplog['$main']
# Uncomment this for replica sets.
#oplog = c.local.oplog.rs

first = next(oplog.find().sort('$natural', pymongo.DESCENDING).limit(-1))
ts = first['ts']

while True:
    cursor = oplog.find({'ts': {'$gt': ts}}, cursor_type=CursorType.TAILABLE_AWAIT, oplog_replay=True)
    while cursor.alive:
        for doc in cursor:
            ts = doc['ts']
            print doc
            # Work with doc here
