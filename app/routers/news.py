import sys

from bson import ObjectId
sys.path.insert(0,'News-System-BE/app/Service')
from os import environ

MONGO_URI = environ.get('MONGO_URI')
DB_NAME = environ.get('DB_NAME')

from flask import Blueprint, jsonify
from Service.mongo import MongoService

news_blueprint = Blueprint('news', __name__,)
mongo_service = MongoService(url=MONGO_URI,database_name=DB_NAME)

@news_blueprint.route('/common-articles',methods=['GET'])
def get_common_articles():
    query = {
        "urlToImage": {"$ne": ""}
    }
    return mongo_service.find(query,{},10)

@news_blueprint.route('/<id>',methods=['GET'])
def get_articles(id):
    query = {
        "_id":ObjectId(id)
    }
    return mongo_service.find_one(query)