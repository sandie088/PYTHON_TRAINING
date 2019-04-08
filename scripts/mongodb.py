import pymongo

clientOjb = pymongo.MongoClient("mongodb://localhost:27017/")

myDb = clientOjb["testdatabase"]

print(clientOjb.list_database_names)

testCollection = myDb["profiles"]
print(myDb.list_collection_names)

testDict = {"profile_id":1, "profile_type":2, "profile_name":"compliance"}
x = testCollection.insert_one(testDict)
print(x.inserted_id)

for x in testCollection.find({}, {"_id":0, "profile_id":1}):
    print(x)

myQuery = {"profile_type": 2}
myDoc = testCollection.find(myQuery)

for x in myDoc:
    print(x)

print('\n')
    
myQuery = {"profile_type": {"$gt": 3}}
myDoc = testCollection.find(myQuery)

for x in myDoc:
    print(x)

print('\n')
    
myQuery = {"profile_name": {"$regex": "^geo"}}
myDoc = testCollection.find(myQuery)

for x in myDoc:
    print(x)

print('\n')

myDoc = testCollection.find({}, {"profile_type": 1}).sort("profile_type", 1) #Ascending
for x in myDoc:
    print(x)

print('\n')

myDoc = testCollection.find({}, {"profile_type": 1}).sort("profile_type", -1) #Descending
for x in myDoc:
    print(x)

print('\n')
    
myQuery = {"profile_type": 2}
myDoc = testCollection.delete_many(myQuery)

for x in testCollection.find():
    print(x)

print('\n')

myQuery = {"profile_name": "geofence"}
newValues = {"$set" : {"profile_name": "geofence policy"}}
testCollection.update_many(myQuery, newValues)

for x in testCollection.find():
    print(x)