import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['sensors']
mycol = mydb['values']
collist = mydb.list_collection_names()
print(list(collist))
