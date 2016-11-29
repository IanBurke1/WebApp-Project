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
Python is a popular interpreted, object-oriented, high level programming language. It's simple and easy to learn. I started learning python before I started the project. Check out [TheNewBoston](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_) for tutorials. 

####Flask
With the help of youtube tutorials, I quickly got the hang of Flask thanks to Bucky from [TheNewBoston](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDi9F_slcQK7knjtO8TUvUs) Youtube channel. 

####HTML and Bootstrap
Once I got the server up and running using Flask, the next step was HTML and designing the page. For me, I usually design the webpage first and add functionality later. I used [Bootstrap](http://getbootstrap.com/) to give me a starter-template for my webpage. Bootstrap is a popular HTML, CSS and JS framework. It is very helpful for developers due to its efficiency. Once the webpage was looking good, I added a bootstrap form for user input. To calculate the BMI I needed the users to enter their height and weight in the form. I then added a Submit button at the bottom so when the user clicks the button, it should calculate their BMI and output the result. 

####Javascript
I had to use javascript to do the math and calculate the BMI and return the result. I encountered a few problems with javascript such as getting html elements and returning elements. I found a solution on Stack Overflow which was very helpful:  http://stackoverflow.com/questions/21698044/basic-bmi-calculator-html-javascript. After I got the calculation working, I then cleaned up the webpage to make it look neat. 

####Database
The next problem was adding a database. I tryed a few open sourced database programs such as [SQLite](https://sqlite.org/), [MongoDB](https://www.mongodb.com/) and [CouchDB](http://couchdb.apache.org/). I couldn't quite get to grips with any of them. It was hard to find any good tutorials on them using flask. I ended up choosing CouchDB and stuck at it. My classmate Andrew, shared a very good link to documentation on using couchdb with python: https://pythonhosted.org/CouchDB/getting-started.html. This got me started and eventually I got a database up and running. The next thing I wanted to incorpeate was getting the user input from the form and storing it into the database. I'm still having problems with it.

### How to run the application
You must install [Python](https://www.python.org/) and [Flask](http://flask.pocoo.org/) first to run the project.

Download and install [CouchDB](http://couchdb.apache.org/) and also install python-couchdb package:
```bash
$ pip install couchdb
```
Download [Curl](https://curl.haxx.se/) to access and transfer data. Enter the curl command below to issue a GET request to your Couchdb :
```bash
$ curl http://127.0.0.1:5984/
```
Get a list of databases:
```bash
$ curl -X GET http://127.0.0.1:5984/_all_dbs
```
To run the application, open up command prompt (CMD) or CMDER and enter:
```bash
$ python webApp.py
```


Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

Vauxton is a visual guide for CouchDB. Enter URL below:
http://127.0.0.1:5984/_utils/



### Architecture
This web application runs in [Python 3](https://www.python.org/) using [Flask](http://flask.pocoo.org/) web micro-framework and uses a open source database [CouchDB](http://couchdb.apache.org/). It uses a [Bootstrap](http://getbootstrap.com/) starter-template including a nav-bar, form and stacked progress bar. 
