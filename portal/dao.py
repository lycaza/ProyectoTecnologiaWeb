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
	
        
def obtener_categorias(conexion):
	try:
		cursor = conexion.execute(" select distinct va.categoria"+
								  " from VentasAgencias va"+								  
								  " order by va.agencia ")
		
		salida= ""
		for row in cursor:
			salida+=str(row[0])+","
		
		return salida
	except Error as e:
		print(e)
	return ""


def obtener_ventas_categorias(conexion):
	try:
		#{ data : [[1,30],[2,15],[3,20],[4,22],[5,12],] , label : 'Categoria 1' },
		strcategorias= obtener_categorias(conexion)
		lscat= strcategorias.split(",")

		salida= "["
		for cat in lscat:

			salida+= "{data:"
			cursor = conexion.execute(" select va.agencia,sum(va.valor_actual_venta)"+
									  " from VentasAgencias va where va.categoria='"+cat+"'"+		
									  "	group by va.agencia"+						  
									  " order by va.agencia ")
		
			i=1		
			salida+="["
			for row in cursor:
				salida+="["+str(i)+","+str(row[1])+"],"
				i= i+1
			salida+="],label:'"+cat+"'},"
		
		salida+= "]"
		
		return salida
	except Error as e:
		print(e)
	return ""



def obtener_lista_agencias(conexion):
	try:
		cursor = conexion.execute(" select va.agencia,sum(va.valor_anterior_venta),sum(va.valor_actual_venta)"+
								  " from VentasAgencias va"+
								  "	group by va.agencia"+								  
								  " order by va.agencia ")
		
		i=1
		salida= ""
		for row in cursor:
			salida+="<tr>"			
			salida+="<td>"+str(i)+"</td>"
			salida+="<td><a href='javascript:valoresAgencia(\""+str(row[0])+"\");'>"+str(row[0])+"</a></td>"
			salida+="<td>"+str(row[1])+"</td>"
			salida+="<td>"+str(row[2])+"</td>"
			salida+="</tr>"

			i= i+1
		
		return salida
	except Error as e:
		print(e)
	return ""