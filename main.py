from flask import Flask , request, render_template,make_response
from flask_restful import Resource, Api, reqparse
import json
from google.cloud import firestore
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


def config_trans_dates(output):
    if output is None:
        return None
    if 'bookingDateTime' in output:
        output['bookingDateTime'] = datetime.datetime.strftime(output['bookingDateTime'],'%Y/%m/%d-%H:%M:%S') 
    if 'valueDateTime' in output:
        output['valueDateTime'] = datetime.datetime.strftime(output['valueDateTime'],'%Y/%m/%d-%H:%M:%S') 
    return output

def return_output(output):
    BAD_REQUEST = {'statusCode':400,'message':'Bad Request'}
    if output is None:
        return BAD_REQUEST, 400
    else:
        return output

def get_transaction_in_range(start_date,end_date):
    return 'nothing'

class getTransactions(Resource):
    def get(self):
        args = request.args
        transaction_id = None
        transaction_id = args.get('transaction_id',None)

        db = firestore.Client()
        transactions = db.collection('users').document('FVj70UDoOThQPsHFTekT').collection('accounts').document('ayLtL7MTTHbdXUjK9wWZ').collection('transactions')
        output = transactions.document(transaction_id).get().to_dict()
        config_trans_dates(output)
        return return_output(output)

def default_dates(start_str,end_str):
    if start_str is not None:
            start = datetime.datetime.strptime(start_str,'%Y-%m-%d')
    else:
        start = datetime.datetime(1950,1,1)

    if end_str is not None:
        end = datetime.datetime.strptime(end_str,'%Y-%m-%d')
    else:
        end = datetime.datetime(3050,1,1)
    return start,end

class getTransactionsInDate(Resource):
    def get(self):
        args = request.args
        transaction_id = None
        start_str = args.get('start',None)
        end_str = args.get('end',None)

        start, end = default_dates(start_str,end_str)

        db = firestore.Client()
        transactions = db.collection('users').document('FVj70UDoOThQPsHFTekT').collection('accounts').document('ayLtL7MTTHbdXUjK9wWZ').collection('transactions')
        docs = transactions.where('bookingDateTime','>',start).where('bookingDateTime','<',end).stream()
        #docs = transactions.stream()
        print('this')

        output_list = []
        for doc in docs:
            print(doc.id)
            trans_dict = doc.to_dict()
            config_trans_dates(trans_dict)
            output_list.append(trans_dict)


        return return_output(output_list)

class Guide(Resource):
    def get(self):
        return make_response(render_template('guide.html') , 200 , {'Content-Type':'text/html'})


api.add_resource(getTransactions, '/get_trans')
api.add_resource(getTransactionsInDate,'/get_trans_in_date')
api.add_resource(Guide,'/')


if __name__ == '__main__':
    app.run(debug=True)