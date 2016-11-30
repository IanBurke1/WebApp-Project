from flask import Flask, render_template, request
import sqlite3 as sql
#import couchdb 

app = Flask(__name__) #Pass in _name_ to help flask determine root path.

#routing/mapping
# @ signifies a decorator - way to wrap a function and modifying its behaviour
@app.route('/') #connect a webpage. '/' is a root directory.
def homepage():

    return render_template("homepage.html") #when user goes to this page return this..


# So i changed from couchDB to using sqlite3 on last minute notice
#The below userinput() function works IF the "Calculate" Button type is changed to type="submit" in the homepage.html
#unfortunately The bmi calculation will not work if the button type is changed from "button" to "submit"

#The below code was taking from a tutorial:  https://www.tutorialspoint.com/flask/flask_sqlite.htm

@app.route('/userinput', methods=['GET','POST']) #Getting info from webpage through POST
def userinput():
    if request.method == 'POST':
        try:
            height = request.form['height'] #users height
            weight = request.form['weight'] #users weight

            with sql.connect("bmi.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user_input (height, height) VALUES (?,?)",(height, weight) )

            con.commit()
        except:
            con.rollback()

        finally:
            return render_template('homepage.html', height=height,weight=weight)
            con.close()
    
if __name__ == '__main__': #quick check to make sure that only run the app whenever this file is called directly
    app.run() #Start this web server
