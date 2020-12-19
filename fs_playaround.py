from google.cloud import firestore
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin


#cred = credentials.Certificate('../.secrets/taxy-298609-506d38f34569.json') 
#firebase_admin.initialize_app(cred)

db = firestore.Client()


db.collection('users').document('FVj70UDoOThQPsHFTekT').collection('accounts').document('ayLtL7MTTHbdXUjK9wWZ').collection('transactions').document('0117656a0ab05q0V').get().to_dict()

transactions = db.collection('users').document('FVj70UDoOThQPsHFTekT').collection('accounts').document('ayLtL7MTTHbdXUjK9wWZ').collection('transactions')

transactions.document('0117656a0ab05q0V').get().to_dict()

def get_transaction_in_range(start_date,end_date):
    return 'nothing'