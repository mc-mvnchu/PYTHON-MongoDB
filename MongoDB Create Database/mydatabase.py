import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient["mydatabase"]

# Executing this file creates DB