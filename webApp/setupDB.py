import couchdb

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')

db = couch.create('user_input')  # create new database
db = couch['user_input'] #existing database

doc = {'_id': 'test'} # Creating a doc
db.save(doc) # Saving it to database