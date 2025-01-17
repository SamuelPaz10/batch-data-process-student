from classes.DbMongo import DbMongo
class Careers:

    def __init__(self, nombre, id = ""):
        self.tipo = nombre
        self.__id = id
        self.__collection = "careers"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_many(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )
        



        