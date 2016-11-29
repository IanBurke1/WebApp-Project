import couchdb

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')

db = couch.create('user_input')
db = couch['user_input']

doc = {'_id': 'test'}
db.save(doc)