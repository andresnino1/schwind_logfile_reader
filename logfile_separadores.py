
#nombre de archivos 2018-02-20__16-37-29.log
# 2018-07-03__11-04-39.log E:\Documents\Python_Schwind\2018-02-20__16-37-29.log


import csv
from pprint import pprint #Esta libreria ayuda a imprimr diccionarios de manera fácil y visualmente estructurada


filename="2018-06-22__15-43-47.log" #asigno la ruta del archivo a la variable fielname

fields=[]                   #creo una lista para las columnas
rows=[]                     #creo una lista para las filas, se guarda cada linea del logfile
values=[]                   #lista para guardar la fila donde estan los valores de fluencia del logfile
num_row_value=[]            #lista que guarda los numeros de lineas donde se encontró valores de fluencia del logfile
num_row=0                   #variable para contar el numero de filas del logfile
values_last_fluence=[]      #es la lista donde estan los valores en bruto de la ultima fluencia, energia, hv etc.. 
fecha_ultima_fluencia=[]    #lista que guarda las fechas donde se encontraron fluencias
hora_ultima_fluencia=[]     #lista que guarda las horas donde se encontraron fluencias -NO USARÉ ESTOS DATOS EN EL FUTURO
lista_pulsos=[]             #Lista que guarda los valroes de pulsos del laser antes de cada fluencia
laser_final={}              #diccionario donde se guardaran los datos finales del laser indexados por fechas

with open(filename, "r") as logfile: #abro el archivo y lo guardo en variable logfile
    #leo logfile con metodo reader de la libreria csv
    #cada elemento estará separado por el delimitador ---> |
    logfile_reader=csv.reader(logfile, delimiter ="|") 

    for row in logfile_reader:  #se recorre todo el archivo linea por linea, row es cada linea
        rows.append(row)    #se va sumando cada linea (row) a la lista de filas (rows)
        
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
    
    
#-----------------------------------------------------------------------------------------------------------------
#EN ESTA PARTE DEL CODIGO SE PREPARA UNA LISTA CON LOS VALORES DE CADA FLUENCIA ENCONTRADA EN EL LOGFILE
#-----------------------------------------------------------------------------------------------------------------
    
    
    count_row_fluencias=0 #Contador para recorrer cada posicion de los rows donde estan las fluencias
    
    for nfluence in values: #recorre cada fluencia encontrada en el logfile
        
        
        #se genera un string o cadena de caracteres 
        #que corresponde al elemento 4 del string que itera los valores donde está cada fluencia
        #como esta lista tiene el titulo FLUENCE VALUES: ---> se quita usando strip("fluence values: ")
        cadena_ultima_fluencia=nfluence[4].strip("Fluence values: ") 
              
    
        #los valores del string estan separados por tres espacios, se genera una LISTA partiendo de la cadena string
        lista_cadena_separadores=cadena_ultima_fluencia.split("   ") 
            
    
    #--------------------------------------------------------------------------------------------
    #EN ESTA PARTE DEL CODIGO SE SACAN LOS DATOS DE LA FECHA Y HORA DE CADA FLUENCIA ENCONTRADA
    #--------------------------------------------------------------------------------------------
    
        #se genera un string o cadena de caracteres que contiene la fecha de la fluencia
        #que corresponde al elemento 0 de la lista que itera los valores donde está cada fluencia
    
        cadena_fecha_ultima_fluencia=nfluence[0]
        
        #se crea una lista de la cadena de la ultima fecha y se dividen en fecha y hora con el separador __
        lista_fecha_hora=cadena_fecha_ultima_fluencia.split("__") 
        
        
        #Se almacena cada fecha en una lista y se va agregando una nueva fecha en cada iteracion
        #la posicon 0 de la lista correspondea a la fecha
        fecha_ultima_fluencia.append(lista_fecha_hora[0])
        
        #Se almacena cada hora en una lista y se va agregando una nueva hora en cada iteracion
        #la posicon 1 de la lista correspondea a la hora
        #ESTOS VALORES NO LOS ESTOY UTILIZANDO EN ESTE PROGRAMA PERO ESTARAN DISPONIBLES SI SE REQUIREN EN EL FUTURO
        hora_ultima_fluencia.append(lista_fecha_hora[1])
    
           
    
    #----------------------------------------------------------------------------------------------------------
    #EN ESTA PARTE DEL CODIGO SE SACAN LOS VALORES DE LOS PULSOS DEL LASER CUANDO SE REALIZÓ LA ULTIMA FLUENCIA
    #----------------------------------------------------------------------------------------------------------
    
    
        #En esta lista estarán almacenados los pulsos del laser que se encuentran en el logfile
        #num_row_value es la lista donde está la información de la linea de cada fluencia encontrada
        #si a esa posición se le restan -4 líneas se llega a la linea donde está la información de los
        #pulsos del laser.
        lista_ultimos_pulsos=rows[num_row_value[count_row_fluencias]-4]
    
        #se saca el string que está en la posicion 4 y se retira el texto sobrante para que solo queden los numeros
        #lista_pulsos es la lista donde estarán almacenados el número de los pulsos
        lista_pulsos.append(lista_ultimos_pulsos[4].strip(" Pulsecounter before FT and DT:"))
  
    
    #-------------------------------------------------------------------------------------------------------------
    # EN ESTA PARTE DEL CODIGO SE SACA LA INFORMACION DE LOS VALORES DEL LASER DE CADA FLUENCIA ENCONTRADA
    # VALORES DE HIGH FLUENCE - LOW FLUENCE - HV - LOW ENERGY - HIGH ENERGY - TEMP
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
        
        #Se agrega el texto Pulses a la lista de indices
        lista_valores_separados_indice.append("Pulses:")
        
        #Se agrega el valor de los pulsos en la lista de valores 
        #la lista se pulsos se va incrementando la posicion usando el contador count_row_fluencias
        lista_valores_separados_valor.append(lista_pulsos[count_row_fluencias])
    
    
    #------------------------------------------------------------------------------------------------
    #EN ESTA PARTE DEL CODIGO SE CREA UN DICCIONARIO PARA FACILITAR EL MANEJO DE LOS VALORES DEL LASER
    #EL DICCINARIO TIENE TODOS LOS VALORES DEL LASER DE LA ULTIMA FLUENCIA- JUNTO CON LA FECHA Y HORA
    #------------------------------------------------------------------------------------------------
    
#        
        #se unen las dos listas de indices y valores para tener un diccionario     
    
        laser_values = dict(zip(lista_valores_separados_indice, lista_valores_separados_valor))
        
        #se actualiza el diccionario FINAL ingresando los valores de cada fecha como INDICE
        #y colocando los valores del diccionario laser_values que corresponde a cada fecha
                
        laser_final.update({fecha_ultima_fluencia[count_row_fluencias]:laser_values})
    
        #se incrementa el condador de lineas de cada fila de fluencias encontrada
        count_row_fluencias=count_row_fluencias+1
    
    
       
    print("Serial: ",serial)
    pprint(dict(laser_final))
    
    
        
    

    


#print("numero de lineas es: %d" %(logfile_reader.line_num))









