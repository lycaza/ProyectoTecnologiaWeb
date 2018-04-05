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
			

def obtener_ventas_agencias(conexion):
	try:
		cursor = conexion.execute(" select va.agencia, sum(va.valor_actual_venta)"+
								  " from VentasAgencias va"+
								  "	group by va.agencia"+
								  " order by va.agencia ")
		
		salida= "["
		for row in cursor:
			salida+="{data:[[0,"+str(row[1])+"]],label:'"+row[0]+"'},"

		salida+="]"

		return salida
	except Error as e:
		print(e)
	return ""


def obtener_indicador(conexion,agencia):	
	try:		
		cursor= conexion.execute("SELECT (((sum(va.valor_actual_venta)/sum(va.valor_anterior_venta))*100)-100) from VentasAgencias va where va.agencia='"+agencia+"' ")
		porcentaje= cursor.fetchone()[0]
		
		return porcentaje
	except Error as e:
		print(e)
	return 0
	
        
