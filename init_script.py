from google.cloud import firestore
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin


cred = credentials.Certificate('../.secrets/taxy-298609-506d38f34569.json') 
firebase_admin.initialize_app(cred)