  
from bson.objectid import ObjectId
from flask import Flask, jsonify, request, Response
from flask.helpers import make_response
from flask_restful import Api, Resource, reqparse, abort, marshal, fields
from pymongo import MongoClient
import json
from bson import json_util
#Prometheus import
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

# Initialize Flask to creat a rest service
app = Flask(__name__)
api = Api(app)
#Prometheus metrics
_INF = float("inf")

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))

@app.route('/')
def ping_server():
    start = time.time()
    graphs['c'].inc()
    
    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    return "Welcome to the world of books."

@app.route("/metrics")
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")    

def create_book(book):
    print(book)
    col = get_db()
    col.insert_one(book)
    return jsonify(message="success")

@app.route('/find')    
def findAll_book():
    col = get_db()
    dict = col.find({})
    ret = ""
    for x in dict:
        ret += json.dumps(x, sort_keys=True, indent=4, default=json_util.default)
    return ret

@app.route('/books', methods=['GET','POST'])
def api_books():
    if request.method == "GET":  #GET return details of books
        print (request.method)
        return make_response (findAll_book(),200)   #200 succss code
    elif request.method == "POST":   #POST create a new book
        create_book(request.json)
        return make_response("Done",201) #return 201 success code (empty response body)

def findA_book(book_id):
    col = get_db()
    dict = col.find({"id": str(book_id)})
    ret = ""
    for x in dict:
        ret += json.dumps(x, sort_keys=True, indent=4, default=json_util.default)
    return ret

def Update(book_id,new_author,new_title):
    col = get_db()
    myquery = { "id": str(book_id) }
    newvalues = { "$set": { "author": new_author, "title": new_title } }
    col.update_one(myquery, newvalues)

def Delete(book_id):
    col = get_db()
    myquery = { "id": str(book_id) }
    col.delete_one(myquery)

@app.route('/books/<book_id>', methods=['GET','PUT','DELETE'])
def api_each_book(book_id):
    if request.method == "GET":
        if findA_book(book_id):
            return make_response (findA_book(book_id),200)   #200 sucess code
        else:
            return make_response ("Your book doesn't exist",404) #404 if not found
    elif request.method == "PUT":
        if findA_book(book_id):
            new_author = request.args.get('author') 
            new_title = request.args.get('title') 
            Update(book_id,new_author,new_title)
            return make_response ("Book updated", 200) #we can here return 204 sucess code but NO CONTENT 
        else:
            return make_response ("Your book doesn't exist",404) #404 if not found
    elif request.method == "DELETE":
        if findA_book(book_id):
            Delete(book_id)
            return make_response ("Delete is done",200)
        else:     
            return make_response ("Your book doesn't exist",404) #404 if not found

def get_db():
    client = MongoClient("mongodb://my_db:27017") #name of db:my_db, default port:27017
    db = client["mk_db"]
    col = db["books"] 
    return col


if __name__ == "__main__":
    app.run(debug=True)        