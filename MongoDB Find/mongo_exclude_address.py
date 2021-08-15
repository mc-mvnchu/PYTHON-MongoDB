import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# To call out DB "mydatabase"
mydb = myclient["mydatabase"]
# To call
mycol = mydb["customers"]

# For loop to disclude the address field from being printed on screen
for x in mycol.find({}, { "address": 0 }):
    print(x)