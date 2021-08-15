import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Syntax to find the "address" field starts with the letter "S", use the RegExp
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

# For loop to find a document where the addresses starts with the letter "S"
for x in mydoc:
    print(x)