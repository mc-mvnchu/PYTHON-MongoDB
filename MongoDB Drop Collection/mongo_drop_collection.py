import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["mydatabase"]
# An unkown collection is inserted to check the boolean result output
mycol = mydb["customing"]

mycol.drop()

print(mycol.drop())
# Outputs `None` because it doesn't exists