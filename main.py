from flask import Flask 
import libraryTesting

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

@app.route("/requestTest")
def reqTest():
    return libraryTesting.requestsAttempt() 


# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")