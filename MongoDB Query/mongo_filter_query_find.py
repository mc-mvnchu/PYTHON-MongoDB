import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# The query is defined with a specific address field
myquery = { "address": "Park Lane 38" }

# Doc is defined with a query.data to find
mydoc = mycol.find(myquery)

# For loop to find the document with the address "Park Lane 38"
for x in mydoc:
    print(x)