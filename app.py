import pymongo
from classes import DATA, Dataprocess, DbMongo, Students, Careers
from dotenv import load_dotenv

def main():

    ### CONNECTION
    client, db = DbMongo.getDB()
    
    ### TRAER LOS DATOS Y GUARDARLOS EN UNA VARIABLE
    pipeline = Dataprocess(DATA)

    
    ## SUBIR A LOS ESTUDIANTES COMO UNA COLECCIÓN
    #pipeline.create_students(db)


    ###########################################
    
    ### CREAR LA COLECCIÓN DE ESTUDIANTES
    #dictEstudiantes = Students.get_dict(db)
    #print(dictEstudiantes)


    ### CREAR LA COLECCIÓN DE CURSOS

    ### CREAR LA COLECCIÓN DE CARRERAS
    carreras = Dataprocess.get_list_students(db)
    #carreras = Students.get_dict(db)
    #carreras.create_careers(db)
    Careers(carreras).save(db)
    #print(carreras)
    

    #pipeline.create_enrollments()

    client.close()
    return True


if __name__ == "__main__":
    load_dotenv()
    main()