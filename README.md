# Basic Web Application Project
#### Data Representation and Querying Project 2016

This repository contains code and information for a third-year undergraduate project for the module **Data Representation and Querying**.
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

### Project overview
The project instructions state:

>You are required to develop a single-page web application (SPA) written in the programming language Python using the Flask framework.

I have created a single-Page Web Application (SPA) that lets users calculate their Body Mass Index (BMI). The reason why I did a BMI calculator is because it is simple to use and easy to work with.

####Python 
Python is a popular interpreted, object-oriented, high level programming language. It's simple and easy to learn. I started learning python before I started the project. Check out [TheNewBoston](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_) for python tutorials. 

####Flask
Flask is a microframework for python. With the help of youtube tutorials, I quickly got the hang of Flask thanks to Bucky from [TheNewBoston](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDi9F_slcQK7knjtO8TUvUs) Youtube channel. 

####HTML and Bootstrap
Once I got the server up and running using Flask, the next step was the HTML file and designing the page. For me, I usually design the webpage first and add functionality later. I used [Bootstrap](http://getbootstrap.com/) to give me a starter-template for my webpage. Bootstrap is a popular HTML, CSS and JS framework. It is very helpful for developers due to its efficiency. Once the webpage was looking good, I added a bootstrap form for user input. To calculate the BMI I needed the users to enter their height and weight in the form. I then added a Submit button at the bottom so when the user clicks the button, it should calculate their BMI and output the result. 

####Javascript
I had to use javascript to do the math for calculating the BMI and return the result. I encountered a few problems with javascript such as getting html elements and returning elements. I found a solution on Stack Overflow which was very helpful:  http://stackoverflow.com/questions/21698044/basic-bmi-calculator-html-javascript. After I got the calculation working, I then cleaned up the webpage to make it look more neat and organised. 

####Database
The next problem was adding a database. I tryed a few open sourced database programs such as [SQLite](https://sqlite.org/), [MongoDB](https://www.mongodb.com/) and [CouchDB](http://couchdb.apache.org/). I couldn't quite get to grips with them. It was hard to find any good tutorials on them using flask. I ended up choosing CouchDB and stuck at it. My classmate Andrew, shared a very good link to documentation on using couchdb with python: https://pythonhosted.org/CouchDB/getting-started.html. This got me started and eventually I got a database up and running. The next thing I wanted to incorperate was getting the user input from the form and storing it into the database. The day before the project submission I changed from using CouchDB back to SQLite3 because I found a good tutorial on SQlite working with Flask:  https://www.tutorialspoint.com/flask/flask_sqlite.htm

###Problems Encountered
**UPDATE:** I was having a problem with passing user form input into a database. I finally figured it out but created another problem. To calculate the BMI I needed to get the height and weight from the form and do the math in javascript. For some reason, the function calculateBmi() wouldn't work if the calculate button on the form was type="submit". When I changed the type to type="Button", the calculation worked and displayed on the page. The other problem was that the method POST wouldn't work if the type was not type="submit" so I couldn't POST the input into the database.

### Curl 
Curl is a tool to transfer data from or to a server using supported protocols. I used curl as another way to access the database. Download [Curl](https://curl.haxx.se/). Enter the curl command below to issue a GET request to your Couchdb :
```bash
$ curl http://127.0.0.1:5984/
```
Get a list of databases:
```bash
$ curl -X GET http://127.0.0.1:5984/_all_dbs
```
Create a database:
```bash
$ curl -X PUT http://127.0.0.1:5984/test
```
Get the database created:
```bash
$ curl -X GET http://127.0.0.1:5984/test
```

### How to run the application
1 You must install [Python](https://www.python.org/) and [Flask](http://flask.pocoo.org/) first to run the project.

2 Download and install [CouchDB](http://couchdb.apache.org/) and also install python-couchdb package:
```bash
$ pip install couchdb
```
3 To run the application, open up command prompt (CMD) or CMDER.

Run setupDB.py
```bash
$ python setupDB.py
```
4 To run the app:
```bash
$ python webApp.py
```

5 Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

6 Vauxton is a visual guide for CouchDB. Enter URL below:
http://127.0.0.1:5984/_utils/



### Architecture
This web application runs in [Python 3](https://www.python.org/) using [Flask](http://flask.pocoo.org/) web micro-framework and uses a open source database [CouchDB](http://couchdb.apache.org/). It uses a [Bootstrap](http://getbootstrap.com/) starter-template including a nav-bar, form and stacked progress bar. [Curl](https://curl.haxx.se/) is used in command lines and scripts to transfer data. 
