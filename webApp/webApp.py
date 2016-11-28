from flask import Flask, render_template, request
import couchdb



app = Flask(__name__) #Pass in _name_ to help flask determine root path.

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/') # Gets the server

#db = couch('bmi') # create new database
db = couch['bmi'] #existing database

#doc = {'name': 'ian'} # Creating a doc
#db.save(doc) # Saving it to database

#routing/mapping
# @ signifies a decorator - way to wrap a function and modifying its behaviour
@app.route('/') #connect a webpage. '/' is a root directory.
def homepage():

    return render_template("homepage.html") #when user goes to this page return this..

@app.route('/bmiCalc', methods=['GET','POST']) #Getting info from webpage through POST
def bmiCalc():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']

        couch = couchdb.Server('http://admin:password@127.0.0.1:5984/_all_dbs')
        db = couch['bmi']
        doc = {id: height}
        doc.save(doc)
        # for id in db:

        return render_template('homepage.html')

if __name__ == '__main__': #quick check to make sure that only run the app whenever this file is called directly
    app.run() #Start this web server
