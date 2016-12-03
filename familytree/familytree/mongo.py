from pymongo import MongoClient
import os

def get_mongo(db='base'):
	client = MongoClient(
	    os.environ['FAMILYTREE_DB2_1_PORT_27017_TCP_ADDR'],
	    int(os.environ['FAMILYTREE_DB2_1_PORT_27017_TCP_PORT']))
	return client[db]
