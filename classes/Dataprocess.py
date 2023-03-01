from classes.DbMongo import DbMongo
from classes.Careers import Careers
from classes.Students import Students

class Dataprocess:

    def __init__(self, data, id = ""):
        #self.nombre = nombre
        self.__data = data
        self.__id = id
        #self.__collection = "students"
        self.__collection = "careers"

    def create_careers(self, db):
        ## Do something to create careers on your mongodb collection using __data
        collection = db["careers"]
        collection.insert_many(self.__dict__)
        #self.__id =  result.inserted_id
        return True

    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        return True

    def create_students(self, db):
        ## Do something to create students on your mongodb collection using __data      
        collection = db[self.__collection]
        collection.insert_many(self.__data)
        return True

    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        return True

    @staticmethod
    def get_list_students(db):
        collection = db["students"]
        estudiantes = collection.find()

        list_students = []
        for e in estudiantes:
            temp_students = Students(
                e["numero_cuenta"]
                , e["nombre_completo"]
                , e["cursos_aprobados"]
                , e["cursos_reprobados"]
                , e["edad"]
                , e["carrera"]
                , e["_id"] 
            )

            list_students.append(temp_students)
        return list_students