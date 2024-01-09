
from flask import jsonify
from pymongo import MongoClient
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re


class MongoService():
    def __init__(self,url,database_name) -> None:
        self.url = url
        self.database_name = database_name
        pass

    def create_client(self):
        self.client = MongoClient(self.url)
    
    def close(self):
        self.client.close()

    def get_list_collections(self):
        self.create_client()
        db = self.client[self.database_name]
        results = db.list_collection_names()
        self.close()
        return results
    
    def insert_new(self,new):
        self.create_client()
        db = self.client[self.database_name]
        new_id = list(db['news'].insert_one(new))
        self.close()
        return new_id
    
    def insert_news(self,news):
        self.create_client()
        db = self.client[self.database_name]
        new_ids= list(db['news'].insert_many(news))
        self.close()
        return new_ids
    
    def find(self,query,exclude,skip,limit):
        self.create_client()
        db = self.client[self.database_name]
        news= list(db['news'].find(query,exclude).skip(skip).limit(limit))
        data = []
        for doc in news:
            doc['_id'] = str(doc['_id'])
            data.append(doc)
        self.close()
        return jsonify(data)

    def find_one(self,query):
        self.create_client()
        db = self.client[self.database_name]
        new= db['news'].find_one(query)
        new['_id'] = str(new['_id'])
        self.close()
        return jsonify(new)
    
    def search_article(self,q,skip,limit):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(q)
        tokens = [w for w in word_tokens if w.lower() not in stop_words and len(w)>1]

        # Tạo biểu thức chính quy để tìm kiếm các token
        regex_pattern = "|".join(map(re.escape, tokens))
        query = {"title": {"$regex": regex_pattern, "$options": "i"}}

        self.create_client()
        db = self.client[self.database_name]
        news= list(db['news'].find(query,{}).skip(skip).limit(limit))
        data = []
        for doc in news:
            doc['_id'] = str(doc['_id'])
            data.append(doc)
        self.close()
        return jsonify(data)