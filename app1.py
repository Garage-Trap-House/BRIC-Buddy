import pyrebase

config = {
  "apiKey": "AIzaSyC1u5LF8UdxWJEkFB1k4y4iA4Njv1c8yck",
  "authDomain": "cs-4800-project.firebaseapp.com",
  "databaseURL": "https://cs-4800-project-default-rtdb.firebaseio.com",
  "projectId": "cs-4800-project",
  "storageBucket": "cs-4800-project.appspot.com",
  "messagingSenderId": "90582600538",
  "appId": "1:90582600538:web:66fbed6394f54ce7848163",
  "measurementId": "G-KZ94TTK7E9"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database() 

#db.child("names").push({"name": "lan"})
#db.child("names").remove()

from flask import * 

app  = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def basic():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
