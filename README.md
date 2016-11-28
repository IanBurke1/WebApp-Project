# Basic Web Application Project
#### Data Representation and Querying Project 2016

This repository contains code and information for a third-year undergraduate project for the module **Data Representation and Querying**.
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

### Project overview
The project instructions state:

>You are required to develop a single-page web application (SPA) written in the programming language Python using the Flask framework.

I have created a single-Page Web Application (SPA) that lets users calculate their Body Mass Index (BMI). The reason why I did a BMI calculator is because it is simple to use and easy to work with. It didn't take long to learn the programming language python as it is easy to understand when I installed it. With the help of youtube tutorials, I quickly got the hang of Flask thanks to Bucky from [The New Boston](https://www.youtube.com/user/thenewboston) Youtube channel. Once I got the server up and running using Flask, the next step was HTML and designing the page. For me, I usually design the webpage first and add functionality later. I used [Bootstrap](http://getbootstrap.com/) to give me a starter-template for my webpage. Bootstrap is a popular HTML, CSS and JS framework. It is very helpful for developers due to its efficiency. Once the webpage was looking good, I added a bootstrap form for user input. To calculate the BMI I needed the users to enter their height and weight in the form. I then added a Submit button at the bottom so when the user clicks the button, it should calculate their BMI and output the result. I had to use javascript to do the math and calculate the BMI and return the result. I encountered a few problems with javascript. I found a solution on Stack Overflow which was very helpful:  http://stackoverflow.com/questions/21698044/basic-bmi-calculator-html-javascript
After I got the calculation working, I then cleaned up the webpage to make it look neat. 
The next problem was adding a database. I tryed a few open sourced database programs such as [SQLite](https://sqlite.org/), [MongoDB](https://www.mongodb.com/) and [CouchDB](http://couchdb.apache.org/). I couldn't get to grips with with any of them. It was hard to find any good tutorials on them. I ended up choosing CouchDB and stuck at it. My classmate Andrew ,shared a very good link to documentation on using couchdb with python: https://pythonhosted.org/CouchDB/getting-started.html. This got me started and eventually I got a database up and running. The next thing I wanted to incorpeate was getting the user input from the form and storing it withing the database. I am still trying to solve this problem.

### How to run the application
Must install [Python](https://www.python.org/) and [Flask](http://flask.pocoo.org/)

### Architecture
This web application runs in [Python 3](https://www.python.org/) using [Flask](http://flask.pocoo.org/) web micro-framework and uses a couchdb database. 
