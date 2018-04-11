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
		cursor= conexion.execute("SELECT (((sum(va.valor_actual_venta)/sum(va.valor_anterior_venta))*100)-100), (((sum(va.valor_actual_venta)/sum(va.valor_anterior_estimado))*100)-100) from VentasAgencias va where va.agencia='"+agencia+"' ")
		arr= cursor.fetchone()
		venta= arr[0] 
		estimado= arr[1]
		
		salida= "{0:.2f}".format(venta)+"|"+"{0:.2f}".format(estimado)		
		return str(salida)
	except Error as e:
		print(e)
	return "0|0"


def obtener_lista_clientes(conexion,agencia):	
	try:		
		maximo=100
		cursor= conexion.execute(" select vc.nombre, vc.valor_actual, vc.latitud, vc.longitud "
									+ " from VentasClientes vc "
									+ " where vc.agencia='" + agencia + "' "
									+ " order by 1,2,3,4 asc "
									+ " limit 1, " + str(maximo))
		i=1
		j=maximo
		salida=""
		
		for row in cursor:
			salida+="["
			salida+="\""+str(row[0]) + "=>$" + str(row[1]) +"\""
			##salida+=","+str(row[1])
			salida+=",\""+str(row[2])+"\""
			salida+=",\""+str(row[3])+"\""
			salida+=","+str(j)
			if i < maximo:
				salida+="],"
			else:
				salida+="]"
				
			i=i+1
			j=j-1
		##salida+="}"	
		return salida
	except Error as e:
		print(e)
	return 0
			

def obtener_indicador_2(conexion,agencia):	
	try:		
		cursor= conexion.execute("SELECT (((sum(va.valor_actual_venta)/sum(va.valor_actual_estimado))*100)-100) from VentasAgencias va where va.agencia='"+agencia+"' ")
		porcentaje_2= cursor.fetchone()[0]
		
		return porcentaje_2
	except Error as e:
		print(e)
	return 0

        
def obtener_categorias(conexion):
	try:
		cursor = conexion.execute(" select distinct va.categoria"+
								  " from VentasAgencias va"+								  
								  " order by va.categoria ")
		
		salida= ""
		for row in cursor:
			salida+="'"+str(row[0])+"',"
		
		salida= salida[:-1]
		return salida
	except Error as e:
		print(e)
	return ""


def obtener_agencias(conexion):
	try:
		cursor = conexion.execute(" select distinct va.agencia"+
								  " from VentasAgencias va"+								  
								  " order by va.agencia ")
		
		salida= ""
		for row in cursor:
			salida+="'"+str(row[0])+"',"
		
		salida= salida[:-1]
		return salida
	except Error as e:
		print(e)
	return ""


def obtener_ventas_categorias(conexion):
	try:
		# {             data : [[1,30],[2,15],[3,20],[4,22],[5,12],] , label : 'Categoria 1'},
		#[{name: 'John',data: [5, 3, 4, 7, 2,5, 3, 4, 7, 2,4,5]}]

		stragencias= obtener_agencias(conexion)
		lsag= stragencias.split(",")

		salida= "["
		for agencia in lsag:

			salida+= "{name:"+agencia+",data:"
			cursor = conexion.execute(" select va.categoria,sum(va.valor_actual_venta)"+
									  " from VentasAgencias va where va.agencia="+agencia+""+		
									  "	group by va.categoria"+						  
									  " order by va.categoria ")
		
			
			salida+="["
			for row in cursor:
				#salida+="["+str(i)+","+str(row[1])+"]," {0:.2f}
				#salida+=str(row[1])+","
				salida+="{0:.2f},".format(row[1])
				
			salida+="]},"
		
		salida+= "]"
		

		strsalida= "["+obtener_categorias(conexion)+"]|"+salida

		return strsalida
	except Error as e:
		print(e)
	return ""



def obtener_lista_agencias(conexion):
	try:
		cursor = conexion.execute(" select va.agencia,sum(va.valor_anterior_venta),sum(va.valor_actual_venta),sum(va.valor_actual_estimado)"+
								  " from VentasAgencias va"+
								  "	group by va.agencia"+								  
								  " order by va.agencia ")
		
		i=1
		salida= ""
		for row in cursor:
			salida+="<tr>"			
			salida+="<td>"+str(i)+"</td>"
			salida+="<td><a href='javascript:valoresAgencia(\""+str(row[0])+"\");'>"+str(row[0])+"</a></td>"
			salida+="<td style='text-align:right'>{0:.2f}</td>".format(row[1])
			salida+="<td style='text-align:right'>{0:.2f}</td>".format(row[2])
			salida+="<td style='text-align:right'>{0:.2f}</td>".format(row[3])
			salida+="</tr>"

			i= i+1
		
		return salida
	except Error as e:
		print(e)
	return ""




def obtener_actual_estimado_categorias(conexion,agencia):
	try:
		#categorias= categorias[:-3]
		
		
		#anterior
		data= "["
		cursor = conexion.execute(" select va.categoria,sum(va.valor_anterior_venta),sum(va.valor_actual_venta),sum(va.valor_actual_estimado)"+
								  " from VentasAgencias va where va.agencia='"+agencia+"'"+										  				  
								  " group by va.categoria order by va.categoria ")
		j=1
		data+="{data:["
		
		for row in cursor:
			data+="["+str(j)+","+str(row[1])+"],"			
			j= j+1			
		data+="],label:'Venta Anterior'},"

		#actual
		cursor = conexion.execute(" select va.categoria,sum(va.valor_anterior_venta),sum(va.valor_actual_venta),sum(va.valor_actual_estimado)"+
								  " from VentasAgencias va where va.agencia='"+agencia+"'"+										  				  
								  " group by va.categoria order by va.categoria ")
		j=1
		data+="{data:["
		for row in cursor:
			data+="["+str(j)+","+str(row[2])+"],"
			j= j+1			
		data+="],label:'Venta Actual'},"

		#estimado
		cursor = conexion.execute(" select va.categoria,sum(va.valor_anterior_venta),sum(va.valor_actual_venta),sum(va.valor_actual_estimado)"+
								  " from VentasAgencias va where va.agencia='"+agencia+"'"+										  				  
								  " group by va.categoria order by va.categoria ")
		j=1
		data+="{data:["
		for row in cursor:
			data+="["+str(j)+","+str(row[3])+"],"
			j= j+1			
		data+="],label:'Venta Estimada'}"
		data+="]"

		print(data)
		return data
	except Error as e:
		print(e)
	return ""