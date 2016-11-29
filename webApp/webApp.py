from flask import Flask, render_template, request, json
import couchdb



app = Flask(__name__) #Pass in _name_ to help flask determine root path.

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/') # Gets the server

db = couch['user_input'] #existing database


#routing/mapping
# @ signifies a decorator - way to wrap a function and modifying its behaviour
@app.route('/') #connect a webpage. '/' is a root directory.
def homepage():

    return render_template("homepage.html") #when user goes to this page return this..

@app.route('/userInput', methods=['GET','POST']) #Getting info from webpage through POST
def userInput():
    if request.method == 'POST':
        height = request.form['height'] #users height
        weight = request.form['weight'] #users weight

       # jsonData = {'Height': height} #Trying to pass in users height and weight. 
        #request.post('http://127.0.0.1:5984/user_input/', data=None, json=jsonData)

        return render_template('homepage.html')

if __name__ == '__main__': #quick check to make sure that only run the app whenever this file is called directly
    app.run() #Start this web server
