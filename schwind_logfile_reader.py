
#nombre de archivos 2018-02-20__16-37-29.log
# 2018-07-03__11-04-39.log


import csv



filename="2018-06-22__15-43-47.log" #asigno la ruta del archivo a la variable fielname

fields=[]  					#creo una lista para las columnas
rows=[] 					#creo una lista para las filas, se guarda cada linea del logfile
values=[]  					#lista para guardar la fila donde estan los valores de fluencia del logfile
num_row_value=[]			#lista que guarda los numeros de lineas donde se encontró valores de fluencia del logfile
num_row=0 					#variable para contar el numero de filas del logfile
values_last_fluence=[] 		#es la lista donde estan los valores en bruto de la ultima fluencia, energia, hv etc.. 



with open(filename, "r") as logfile: #abro el archivo y lo guardo en variable logfile
	#leo logfile con metodo reader de la libreria csv
	#cada elemento estará separado por el delimitador ---> |
	logfile_reader=csv.reader(logfile, delimiter ="|") 

	for row in logfile_reader:  #se recorre todo el archivo linea por linea, row es cada linea
		rows.append(row)	#se va sumando cada linea (row) a la lista de filas (rows)
		
		#si se encuentra el valor 2116-042 que es donde estan los datos de fluencia se mete esa linea (row) en la lista values
		if "2116-042" in row:  
			values.append(row) #en esta lista estarán listados todos los valores de fluencia del logfile
			num_row_value.append(num_row)

		#si se encuentra el valor 2102-021 que es donde estan los datos del serial se mete esa linea (row) en la variable serial_list
		if "2102-021" in row:
			serial_list=row #en esta lista estará la fila con el valor de la version del software y el serial del laser

		num_row=num_row+1 #incrementa el contador del numero de filas del logfile


		

if values==[]:
	print("este logfile no contiene valores de fluencia") #si el archivo no tiene el valor se genera este mensaje

else:
	

#-----------------------------------------------------------------------------------------------------------------
#EN ESTA PARTE DEL CODIGO SE PREPARA UNA LISTA CON LOS VALORES DE LA ULTIMA FLUENCIAR
#-----------------------------------------------------------------------------------------------------------------


	#se crea una nueva lista ULTIMA_FLUENCIA con la fila de la ultima fluencia encontrada
	ultima_fluencia=values[len(values)-1] 
	#print(ultima_fluencia)


	#se genera un string o cadena de caracteres 
	#que corresponde al elemento 4 de la lista donde está la última fluencia
	#como esta lista tiene el titulo FLUENCE VALUES: ---> se quita usando strip("fluence values: ")

	cadena_ultima_fluencia=ultima_fluencia[4].strip("Fluence values: ")
	#print(cadena_ultima_fluencia)
	

	#los valores del string estan separados por tres espacios, se genera una LISTA partiendo de la cadena string
	lista_cadena_separadores=cadena_ultima_fluencia.split("   ") 
	#print(lista_cadena_separadores)


#--------------------------------------------------------------------------------------------
#EN ESTA PARTE DEL CODIGO SE SACAN LOS DATOS DE LA FECHA Y HORA DE LA ULTIMA FLUENCIA
#--------------------------------------------------------------------------------------------

	#se genera un string o cadena de caracteres que contiene la fecha de la última fluencia
	#que corresponde al elemento 0 de la lista donde está la última fluencia

	cadena_fecha_ultima_fluencia=ultima_fluencia[0]

	#se crea una lista de la cadena de la ultima fecha y se dividen en fecha y hora con el separador __
	lista_fecha_hora=cadena_fecha_ultima_fluencia.split("__") 
	
	#la posicion 0 de la lista corresponde a la fecha y esta se guarda en una variable 
	fecha_ultima_fluencia=lista_fecha_hora[0]
	
	#la posicion 1 de la lista corresponde a la hora y se guarda en una variable
	hora_ultima_fluencia=lista_fecha_hora[1]

	# print(fecha_ultima_fluencia)
	# print(hora_ultima_fluencia)


#----------------------------------------------------------------------------------------------------------
#EN ESTA PARTE DEL CODIGO SE SACAN LOS VALORES DE LOS PULSOS DEL LASER CUANDO SE REALIZÓ LA ULTIMA FLUENCIA
#----------------------------------------------------------------------------------------------------------


	#len(num_row_value)-1 ---> posicon en lista donde esta el numero de linea donde están los ultimos valores de fluencia
	#print(rows[num_row_value[len(num_row_value)-1]-4]) #lugan donde esta el valor de los pulsos
	#resto - 4 --> porque el valor de los pulsos esta a 4 posiones anteriores al valor de la ultima fluencia
	lista_ultimos_pulsos=rows[num_row_value[len(num_row_value)-1]-4]

	#se saca el string que está en la posicion 4 y se retira el texto sobrante para que solo queden los numeros
	pulsos=lista_ultimos_pulsos[4].strip(" Pulsecounter before FT and DT:")
	#print(pulsos)
	

#-----------------------------------------------------------------------------------------------------
#EXTRAER EL SERIAL DEL LASER
#SE ENCUENTRA BUSCANDO ESTE CODIGO --> 2102-021
#--------------------------------------------------------------------------------------------------------
	#print(serial_list)
	# se guarda el string de la posicion 4 de la lista, esta posicion se encuentra el serial
	cadena_serial=serial_list[4] 
	# se encuentra el numero de posicion en la cadena de caracteres del la palabra (ini): ya que 
	#despues de esta palabra se encuentra el serial del laser
	position_serial=serial_list[4].find("(ini):")  
	#se filtra la cadena de caracteres contando 6 lugares despues de la posicion de la palabra (ini):
	#y el valor que se encuentra es el numero serial del laser
	serial=cadena_serial[position_serial+6:]

#-------------------------------------------------------------------------------------------------------------
# EN ESTA PARTE DEL CODIGO SE SACA LA INFORMACION DE LOS VALORES DEL LASER EN SU ULTIMA FLUENCIA
# VALORES DE HIGH FLUENCE - LOW FLUENCE - HV - LOW ENERGY - HIGH ENERGY 
#------------------------------------------------------------------------------------------------------------- 
	
	
	lista_valores_separados_indice=[] #lista donde estarán guardados los indices 
	lista_valores_separados_valor=[] #lista donde estaran guardados los valores de cada indice
	count_index=0 #un contador necesario para recorrer cada numero de posición de la lista de la cadena de separadores

	for i in lista_cadena_separadores: #se recorre cada fila de la lista de la cadena

		#se crea una variable string para guardar la informacion del indice y valor
		#es decir, en la fila 0 (count_index) estará el primer valor -- > High Fluence:444
		#en la fila 1 (count_index) etará el segundo valor -- > Low Fluende:111
		#en la fila 2 (count_index) estará el tercer valor -- > HV:111  etc... etc.. 
		indice_valor=lista_cadena_separadores[count_index] 

		#cada strig se divide con los separadores ":" esto para separar el indice y el valor
		#y estos valores se guardan en una lista
		lista_valores_separados=indice_valor.split(":")

		#los indices se guardaran en la lista_valores_separados_indice
		#esta lista se llenará con los valores de la posicion 0 de la lista de valores separados
		#la cual contiene los índices
		lista_valores_separados_indice.append(lista_valores_separados[0])

		#los valores se guardaran en la lista_valores_separados_valor
		#esta lista se llenará con los valroes de la posicion 1 de la lista de valores separados
		#la cual contiene los valores
		lista_valores_separados_valor.append(lista_valores_separados[1])
		count_index=count_index+1


	# print(lista_valores_separados)

	# print(lista_valores_separados_indice)
	# print(lista_valores_separados_valor)

#------------------------------------------------------------------------------------------------
#EN ESTA PARTE DEL CODIGO SE CREA UN DICCIONARIO PARA FACILITAR EL MANEJO DE LOS VALORES DEL LASER
#EL DICCINARIO TIENE TODOS LOS VALORES DEL LASER DE LA ULTIMA FLUENCIA- JUNTO CON LA FECHA Y HORA
#------------------------------------------------------------------------------------------------

	laser_values = dict(zip(lista_valores_separados_indice, lista_valores_separados_valor))
	laser_values.update( {"fecha" : fecha_ultima_fluencia, "hora" : hora_ultima_fluencia, "pulsos": pulsos, "serial": serial} )
	#print (laser_values)

	#print(laser_values)
	print("Serial: ", laser_values["serial"])
	print("Fecha: ", laser_values["fecha"])
	print("Hora: ", laser_values["hora"])
	print("High Fluence: ", laser_values["High Fluence"])
	print("Low Fluence: ", laser_values["Low Fluence"])
	print("HV: ", laser_values["HV"])
	print("HI Energy: ", laser_values["E_preset_HI "])
	print("Low Energy: ", laser_values["E_preset_LO "])
	print("Pulsos: ", laser_values["pulsos"])


		
	

	


#print("numero de lineas es: %d" %(logfile_reader.line_num))









