from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    
    def __init__(self, username, userpassword):
        userName =  username
        password = userpassword
        self.client = MongoClient('mongodb://%s:%s@localhost:30218/?authSource=AAC' %(userName,password))
        self.database = self.client['AAC']
        
    #implements Create in CRUD  
    def createDocument(self, data=None):
        if data is not None:
            insertDocument = self.database.animals.insert_one(data)
            return True if insertDocument.acknowledged else False
        else:
            raise Exception("Can not create Document, data field left empty")
            
    #implements Read in CRUD
    def getDocuments(self, data = None):
        if data is not None:
            query = self.database.animals.find(data,{'_id':False})
        else:
            query = self.database.animals.find({},{'_id':False})
        return query
    #implements Update in CRUD
    def updateDocuments(self, query, updatedValue):
        
        if not query:
            raise Exception("please include query search")
        if not updatedValue:
            raise Exception("please inlcude a value to update")
        toBeUpdated = self.getDocuments(query)
        for documents in toBeUpdated:
            print(documents)
        print("Result:")
        validUpdate = self.database.animals.update_many(query,{"$set": updatedValue})
        
        print(validUpdate.raw_result)
        
        return True
        
    #implements Delete in CRUD
    def deleteDocument(self, query):
        if not query:
            raise Exception("please include Query to delete")
        toBeDeleted = self.getDocuments(query)
        for documents in toBeDeleted:
            print(documents)
        validDelete = self.database.animals.delete_many(query)
        print("Result of deletion:")
        print(validDelete.raw_result)
        return True