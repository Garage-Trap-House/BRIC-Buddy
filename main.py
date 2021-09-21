from flask import Flask 

# make the flask app 
app = Flask(__name__)

# Bryant's HTTP request
@app.route("/hello_world")
def hello_world(): 
    return "The Garage Trap House says hi! :)"



# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")