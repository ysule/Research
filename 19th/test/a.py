from pymongo import MongoClient
from pymongo.cursor import _QUERY_OPTIONS
from pymongo.errors import AutoReconnect
from bson.timestamp import Timestamp

# Tailable cursor options.
_TAIL_OPTS = {'tailable': True, 'await_data': True}

# Time to wait for data or connection.
_SLEEP = 10

if __name__ == '__main__':
    db = MongoClient().local

    while True:
        query = {'ts': {'$gt': Timestamp(1463115114, 0)}}  # Replace with your query.
        cursor = db.oplog.rs.find(query, **_TAIL_OPTS)

        cursor.add_option(_QUERY_OPTIONS['oplog_replay'])

        try:
            while cursor.alive:
                try:
                    doc = next(cursor)

                    # Do something with doc.

                except (AutoReconnect, StopIteration):
                    sleep(_SLEEP)

        finally:
            cursor.close()