from flask import Flask, render_template, request
import couchdb



app = Flask(__name__) #Pass in _name_ to help flask determine root path.

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/') # Gets a server 


db = couch.create('bmi') # create new database

doc = {'name': 'ian'}
db.save(doc)

#routing/mapping
# @ signifies a decorator - way to wrap a function and modifying its behaviour
@app.route('/') #connect a webpage. '/' is a root directory.
def homepage():

    return render_template("homepage.html") #when user goes to this page return this..

@app.route('/bmiCalc', methods=['GET','POST'])
def bmiCalc():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
      #  result = request.form['result']

       # with sql.connect("bmi.db") as con:
        #    cur = con.cursor()
         #   cur.execute("INSERT INTO bmi_results (height, weight) VALUES (?,?)",(height, weight) )

#            con.commit()

        return render_template('homepage.html')

    #return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__': #quick check to make sure that only run the app whenever this file is called directly
    app.run() #Start this web server
