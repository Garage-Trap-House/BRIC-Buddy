
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import * 

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}
db.collection('persons').document('names').set(data)
#db.collection('persons').document('fiLxfhdcgJguDe6HLkLb').delete()
#db.collection('persons').document('m3sov2h6vhkJRwoE71Bm').delete()
#db.collection('persons').document('xvkjFMmVi5EuvetNzD11').delete()



