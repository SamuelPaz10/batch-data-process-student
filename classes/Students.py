from classes.DbMongo import DbMongo

class Students:

    def __init__(self, numero_cuenta, nombre_completo, cursos_aprobados, cursos_reprobados, edad, carrera, data):
        self.numero_cuenta = numero_cuenta
        self.nombre_completo = nombre_completo
        self.cursos_aprobados = cursos_aprobados
        self.cursos_reprobados = cursos_reprobados
        self.edad = edad
        self.carrera = carrera
        self._data = data
        self.__collection = "Students"

    def create_students(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    @staticmethod
    def get_dict(db):
        collection = db["students"]
        estudiantes = collection.find()

        list_estudiantes = []
        for e in estudiantes:
            temp_estudiante = Students(
                e["numero_cuenta"]
                , e["nombre_completo"]
                , e["cursos_aprobados"]
                , e["cursos_reprobados"]
                , e["edad"]
                , e["carrera"]
            )

            list_estudiantes.append(temp_estudiante)
        return list_estudiantes

    