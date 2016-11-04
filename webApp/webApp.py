from flask import Flask, render_template

app = Flask(__name__) #Pass in _name_ to help flask determine root path.

#routing/mapping
# @ signifies a decorator - way to wrap a function and modifying its behaviour
@app.route('/') #connect a webpage. '/' is a root directory.
def homepage():
    return render_template("homepage.html") #when user goes to this page return this..


if __name__ == '__main__': #quick check to make sure that only run the app whenever this file is called directly
    app.run() #Start this web server
