# coding:utf-8
import pymongo

client = pymongo.MongoClient(host='localhost', port='27017')
db = client.testdb
collection = db.beikao
student = {
    '_id': 1,
    'name': 'python',
    'age': 200,
}
result=collection.insert(student)
print(result)
