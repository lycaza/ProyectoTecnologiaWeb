#from models import Usuario
import sqlite3
from sqlite3 import Error

def create_connection(db_file):   
        try:
            conn = sqlite3.connect(db_file)
            print("Opened database successfully")
            return conn
        except Error as e:
            print(e)
     
        return None


def verifica(conexion,usuario,clave):   
        try:
            cursor = conexion.execute("SELECT count(*) from usuarios where usuario='"+usuario+"' and clave='"+clave+"' ")
            count= cursor.fetchone()[0]
                      
            if count > 0:
            	return True
            else:
            	return False
        except Error as e:
            print(e)     
        return False


           	#cursor = conn.execute("SELECT count(*) from usuarios where usuario='"+usuario+"' and clave='"+clave+"' ")
			#for row in cursor:
			#   print("ID = ", row[0])
			#   print("NAME = ", row[1], "\n")
			
	
     
        
