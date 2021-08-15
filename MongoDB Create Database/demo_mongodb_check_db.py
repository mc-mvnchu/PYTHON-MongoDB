import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

#print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
