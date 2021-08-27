import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Delete All Documents in a collection
x = mycol.delete_many({})

print(x.delete_count, " documents deleted.")
# Outputs a print of the total number of deleted documents deleted == all documents