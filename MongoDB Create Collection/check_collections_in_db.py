import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

mycol = mydb["customers"]

# Collection created

# Syntax to check the list of collection in your database:
print(mydb.list_collection_names())
