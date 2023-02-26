import pymongo
from classes import DATA, Dataprocess, DbMongo, Students
from dotenv import load_dotenv

def main():

    ### CONNECTION
    client, db = DbMongo.getDB()
    
    ### TRAER LA DATA
    pipeline = Dataprocess(DATA)
    
    ## SUBIRLO COMO UNA COLECCIÓN
    pipeline.create_data(db)


    ###########################################
    
    ### CREAR LA COLECCIÓN DE ESTUDIANTES
    #dictEstudiantes = Students.get_dict(db)
    #print(dictEstudiantes)


    ### CREAR LA COLECCIÓN DE CURSOS

    ### CREAR LA COLECCIÓN DE CARRERAS
    #pipeline.create_careers()
    
    #pipeline.create_enrollments()


   
    client.close()
    
    return True

    

if __name__ == "__main__":
    load_dotenv()
    main()