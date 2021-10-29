import pymongo
from pymongo import MongoClient

class DB:
	def __init__(self,host="localhost",port="5010"):
		self.client = MongoClient("mongodb://{}:{}/".format(host,port))
	def query(self, search_object={"name":"Trâm"}):
		chatbot_db = self.client.chatbot_db.user
		found_obj = chatbot_db.find_one(search_object)
		return found_obj 
