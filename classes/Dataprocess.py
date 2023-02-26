

class Dataprocess:

    def __init__(self, data):
        self.__data = data
        self.__collection = "DATA"

    def create_careers(self, db):
        ## Do something to create careers on your mongodb collection using __data
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        return True

    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        return True
    
    def create_students(self, db):
        ## Do something to create students on your mongodb collection using __data      
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        return True
    

    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        return True
    
    ###Sin modificar
    @staticmethod
    def get_list(db):
        collection = db["estudiante"]
        estudiantes = collection.find()

        list_estudiantes = []
        for e in estudiantes:
            temp_estudiante = Dataprocess(
                e["nombre"]
                , e["apellido"]
                , e["telefono"]
                , e["tipo_estudiante"]
                , e["_id"] 
            )

            list_estudiantes.append(temp_estudiante)
        return list_estudiantes
    
        
    def create_data(self, db):
        ## Do something to create students on your mongodb collection using __data        
        collection = db[self.__collection]
        tipos = collection.find()