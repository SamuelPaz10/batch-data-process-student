from classes.DbMongo import DbMongo

class Students:

    def __init__(self, account, name, approved_course, reprobate_course, age, career, id = ""):
        self.account = account
        self.name = name
        self.approved_course = approved_course
        self.reprobate_course = reprobate_course
        self.age = age
        self.career = career
        self.id = id
        self.__collection = "Students"

    def create_students(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    ##@staticmethod
    def get_dict(self,db):
        collection = db["DATA"]
        tipos = collection.find()

        dict_tipo_estudiantes = {}
        for e in tipos:
            dict_tipo_estudiantes[e] 
            dict_tipo_estudiantes = collection.insert_one(self.__dict__)

        return dict_tipo_estudiantes

    