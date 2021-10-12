from flask import Flask 
import libraryTesting
from arrowTest import *
import mathTest
from Weather import *

import numpyTest

# make the flask app 
app = Flask(__name__)

# Bryant's HTTP request
@app.route("/hello_world")
def hello_world(): 
    return "The Garage Trap House says hi! :)"

#Vincent's HTTP request
@app.route("/deez")
def deez(): 
    return "Deez nuts. Hah gotem!"

#Talha's HTTP request
@app.route("/yaa_u")
def yaa_u(): 
    return "yaa"

#Abdul's HTTP request
@app.route("/abdul")
def abdul():
    return "Yo its ya boi Abdul"

#Lan's HTTP request
@app.route("/lan")
def lan():
    return "Hello! This is Lan :DDDD"

#Lan's library example
@app.route("/math")
def math():
    n = 2
    m = 5 
    return mathTest.mathAttempt(n,m)

@app.route("/requestTest")
def reqTest():
    return libraryTesting.requestsAttempt() 

@app.route("/numpy")
def numpy():
    return numpyTest.numpyAttempt() 

#Abdul's library example
@app.route("/time")
def time():
    return currentTime()

@app.route("/funcToTest")
def funcToTest():
    x = 4
    y = -8
    return mathTest.abdulAttempt(x,y)

#Talha's library example
@app.route("/weather")
def weather():
    return currentWeather()


# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")


