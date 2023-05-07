from utilidadesA import *
from validaciones import *


def obtener_fecha():

    """
    Sinopsis:
        Función que permite obtener la fecha exacta del dispositivo


    Entradas y salidas:
        - returns: ahora, fecha del equipo
    """

    from datetime import datetime
    ahora = str(datetime.now())
    return ahora[0:10]

def solicitar_fecha():

    """
    Sinopsis:
        Función que le solicita al usuario una fecha y verifica si es o no valida


    Entradas y salidas:
        - returns: fecha si la misma es valida 
    """

    estado = False
    while estado != True:
        fecha = input("Ingrese la fecha en el formato YYYY-MM-DD: ")
        estado = validar_fecha(fecha)
        if estado != True:
            print("Ingrese una fecha valida")
    return fecha

def respuesta_numerica(string,digitos_validos_str):

    """
    Sinopsis:
        Función que permite validar si el usuario ingresa un número de un 
        conjunto especifico dado como argumento


    Entradas y salidas:
        - digitos_validos_str: conjunto de números validos en str
        - string: texto que se mostrará por pantalla al ejecutar el input
        - returns: num
    """

    num = ""
    while num not in digitos_validos_str or len(num) != 1 or len(num) != 1:
        num = input(string)
        if num not in digitos_validos_str or len(num) != 1:
            print("La opción no es valida")
            print("-Seleccione Nuevamente-")
            print("----------------------")
    return num

def generar_codigo(diccionario):

    """
    Sinopsis:
        funcion que usa el diccionarion de estaciones, itera entre todos las claves que 
        corresponden a los códigos y retorna un número mayor que el código mayor del diccionario.


    Entradas y salidas:
        - diccionario: diccionario de estaciones
        - returns: nuevo código compatible con los requerimientos
    """

    if len(diccionario) == 0:
        return "1"
    
    mayor = 0
    for clave in diccionario:
        if int(clave) > mayor:    
            mayor = int(clave)
        cod = mayor + 1
    return str(cod)

def extraer_usuarios(archivo,diccionario):

    """
    Sinopsis:
        funcion que nos extraer los usuarios del archivo registros.txt siguiendo de manera estricto 
        las caracteristicas de la plantilla

    Entradas y salidas:
        - archivo: archivo de dónde se extraerá la información
        - diccionario: diccionario donde se almacenará la información
        - returns: none: se realizan los cambios durante la ejecución
    """

    file = open_file(archivo)
    indice = 0
    maxIndice = posLineWhite(archivo)[0]
    
    while indice != maxIndice:
        linea = file[indice].rstrip()
        linea = linea[1:-1]
        elementos = custom_split(linea,";")
        diccionario[elementos[0]] = {'usuario': elementos[1], 'contrasena': elementos[2], 'rol': elementos[3]}
        indice += 1

def extraer_departamentos(archivo):

    """
    Sinopsis:
        funcion que nos extrae los departamentos disponibles de la base de datos

    Entradas y salidas:
        - archivo: archivo de dónde se extraerá la información
        - returns: lista con departamentos
    """

    file = open_file(archivo)
    indice = posLineWhite(archivo)[1]-1
    linea = file[indice].rstrip()
    linea = linea[1:]
    departamentos = custom_split(linea,",")
    return departamentos

def extraer_estaciones(archivo,diccionario):

    """
    Sinopsis:
        funcion que nos extraer las estaciones del diccionario

    Entradas y salidas:
        - archivo: archivo de dónde se extraerá la información
        - returns: lista con departamentos
    """

    file = open_file(archivo)
    indice = posLineWhite(archivo)[1]+1   #Desde la primera linea en blanco que va a extraer las posiciones
    maxIndice = posLineWhite(archivo)[2]  #Hasta la ultima linea en blanco que va a extraer posiciones
    linea = file[indice].rstrip()
    
    lecturas =  extraer_lecturas(archivo)
    
    #####################################
    #Aqui simplemente llamamos los tipos de variable para meterlos en una lista para meterlos al diccionario de estaciones
    #para que no quede asi por si depronto cambian la variable de medicion
    #diccionario[clave]['mediciones'][lecturas[i][0]] = {"PM10" : variables1[0] , "PM25":variables1[1],"Temperatura" : variables1[2],"Humedad" : variables1[3], }
    tiposDeVariables = extraer_tipo_variable(archivo)
    #¨print(tiposDeVariables)
    bandera = True
    acumulador=""
    listaVariables = []
    
    for i in tiposDeVariables:
        for j in i:
            if j == "]":
                bandera = True
            elif j == "[":
                bandera = False
                listaVariables.append(acumulador)
                acumulador = ""
            elif bandera:
                acumulador = acumulador + j
            
    #####################################¨
    
    #####################################
    while indice != maxIndice:
        linea = file[indice].rstrip()
        elementos = custom_split(linea,",")
       
        diccionario[elementos[0]] = {'nombre_estacion': elementos[1], 'municipio': elementos[2], 'mediciones':{}}
        indice += 1 
    contador=1
    
    #Relacionaamos las lecturas que tenemos o mediciones con las estaciones
    for clave in diccionario: #recorremos el diccionario para ver las claves
        for i in range(len(lecturas)):   #recorremos cada uno de lecturas para mirar su id y compararlo con el de la clave del diccionario 
            id = lecturas[i][1] #colocamos el 1 ya que lectura es una lista que tiene otras listas entonces el i para alternar entre esas listas y el 1 para la posicion del id
            if clave == id:
                diccionario[clave]['mediciones'][lecturas[i][0]] = {} #Creamos una clave (es la fecha o fechas) para meter las variables
                variables = lecturas[i][2]   #Sacamos las mediciones de la lista x
                variables1 = custom_split(variables[1:-1],",") #hacemos una lista con las variables de la lista
                #diccionario[clave]['mediciones'][lecturas[i][0]] = {listaVariables[0] : variables1[0] , "PM25":variables1[1],"Temperatura" : variables1[2],"Humedad" : variables1[3], }
                diccionario[clave]['mediciones'][lecturas[i][0]] = {listaVariables[0] : variables1[0] , listaVariables[1]:variables1[1],listaVariables[2]: variables1[2],listaVariables[3]: variables1[3], }
                


    # j = 0

    # for j in range(len(lecturas)):
    # #Acedemos a cada uno de las variables 
    #     variables = lecturas[j][2]
    # #Como esos valores vienen juntos, entonces los separamos y con el slicing quitamos los {}
    #     variables1 = custom_split(variables[1:-1],",") #[3.5,6.2,27.0,34.0]
    # #Variables 1 es el retorno del split que es una lista de esas variables, entonces como el PM10 esta en la posicion 0 de la lista colocamos esa 

    # diccionario[clave]['mediciones'][lecturas[j][0]] = {"PW10" : variables1[0] }


    


            



def extraer_tipo_variable(archivo):

    """
    Sinopsis:
        funcion que nos extrae los tipos de variables disponibles a analizar de la base de datos

    Entradas y salidas:
        - archivo: archivo de dónde se extraerá la información
        - returns: lista con los tipos de variable
    """

    file = open_file(archivo)
    indice = posLineWhite(archivo)[2]+1
    linea = file[indice].rstrip()
    lecturas = custom_split(linea,";")
    return lecturas

def extraer_lecturas(archivo):

    """
    Sinopsis:
        funcion que nos extraer las lecturas de la base de datos

    Entradas y salidas:
        - archivo: archivo de dónde se extraerá la información
        - returns: lista con las lecturas
    """

    file = open_file(archivo)
    indice = posLineWhite(archivo)[3]+1
    maxIndice = len(file)
    lista = []

    while indice != maxIndice:
        linea = file[indice].rstrip()
        lista.append(custom_split(linea,";"))
        indice += 1
    return lista


#   print(extraer_lecturas("registros_.txt"))
# print(extraer_tipo_variable("registros_.txt"))





def input_valor_validacion(string):
    
    """
    Sinopsis:
        Función que permite validar si un string se puede castear a un número valido
        , si el se toma como argumento ND o ND la funcion retorna ND


    Entradas y salidas:
        - string: valor para hacer la comprobación
        - returns: numero en entero o ND en ese caso particular
    """

    caracteres = "0123456789NDnd"
    contCaracteresInvalidos = 1

    while contCaracteresInvalidos != 0:
        contCaracteresInvalidos = 0
        p = input(string, )
        for caracter in p:
            if caracter not in caracteres:
                contCaracteresInvalidos += 1
                print("Ingrese un valor valido")
                break
        if p.upper() == "ND":
            return "ND" 
    return int(p)

def input_variable_medicion(tipo):

    """
    Sinopsis:
        funcion que permite solicitar al usuario que ingrese cualquiera de los 4 tipos 
        de variables. 


    Entradas y salidas:
        - tipo: tipo de variable denotado con un numero:
        0.PM25
        1.PM30
        2.Temperatura
        3.Humedad
        - returns: valor de la variable
    """

    estado = True
    if tipo == 0:
        while estado:
            var = input_valor_validacion("Ingrese la medición de PM10 en ug/m3:")   
            if type(var) == str:
                return -999
            if validacion_rango(var,0.0,100.0):
                estado = False
            if validacion_rango(var,0.0,100.0) == False:
                print("Ingrese un valor valido")

    elif tipo == 1:
        while estado:
            var = input_valor_validacion("Ingrese la medición de PM25 en ug/m3:")
            if type(var) == str:
                return -999
            if validacion_rango(var,0.0,200.0):
                estado = False
            if validacion_rango(var,0.0,200.0) == False:
                print("Ingrese un valor valido")

    elif tipo == 2:
        while estado:
            var = input_valor_validacion("Ingrese la medición de temperatura en °C:")
            if type(var) == str:
                return -999
            if validacion_rango(var,-20.0,50.0):
                estado = False
            if validacion_rango(var,-20,50.0) == False:
                print("Ingrese un valor valido")

    elif tipo == 3:
        while estado:
            var = input_valor_validacion("Ingrese la medición de humedad en %:")
            if type(var) == str:
                return -999
            if validacion_rango(var,0.0,100.0):
                estado = False
            if validacion_rango(var,0.0,100.0) == False:
                print("Ingrese un valor valido")

    return var

def registrar_mediciones(diccionario,codigo):

    """
    Sinopsis:
        Función permite ingresar mediciones como valor a un diccinario previamente definido


    Entradas y salidas:
        - diccionario: diccionario base
        - codigo: codigo de la estacion
        - returns: no hay, se realizan las actualizaciones correspondientes
    """

    dirM = {}
    lista_valores = []
    fecha = obtener_fecha()
    lista_mediciones = []

    for i in range(0,4):
        valores = input_variable_medicion(i)
        lista_valores.append(valores)
    
    dirM[fecha] = {'PM10':lista_valores[0],'PM25':lista_valores[1],'temperatura':lista_valores[2],'humedad':lista_valores[3]}
    lista_mediciones.append(dirM)

    diccionario[codigo]["mediciones"] += lista_mediciones

def listar_mediciones(dir_estaciones,codigo):

    """
    Sinopsis:
        Función permite listar las medidas de cierta estación dada como código


    Entradas y salidas:
        - dir_estaciones: diccionario base
        - codigo: codigo de la estacion
        - returns: no hay, se realizan las impresiones de la información correspondiente

        -ES POSIBLE QUE SE HAGAN CAMBIOS EN LA FUNCION PARA IMPRIMIR LA INFORMACION EN TABLAS, PERO POR AHORA PERMANECE ASÍ
    """

    mediciones = dir_estaciones[codigo]["mediciones"]
    for i in mediciones:
        for j in i:
            print("El día:", j, "las mediciones fueron:", "PM10:", i[j]["PM10"], "PM25:", i[j]["PM25"], "Temperatura", i[j]["temperatura"], "Humedad", i[j]["humedad"])


def MedicionFechaEspecifica(diccionario, variable, fecha, codigo):
    """
    Sinopsis:
        Función permite ver el valor de una variable en un día especifico

    Entradas y salidas:
        - diccionario: diccionario base que contiene la información
        - variable: variable que se desea consultar
        - fecha: fecha que se desea consultar
        - codigo: código del objeto que se desea consultar
        - returns: none, se imprime el valor de la variable en la fecha seleccionada
    """


    valores = []
    for medicion_fecha, medicion_valores in diccionario[codigo]['mediciones'].items():
        if medicion_fecha == fecha:
            if variable in medicion_valores and medicion_valores[variable] != -999:
                valores.append(medicion_valores[variable])
    if valores:
        print(f'El valor de la {variable} para la fecha {fecha} es {valores[0]}')
    else:
        print(f'No hay mediciones de la variable {variable} para la fecha {fecha} en la estacion que lleva por código {codigo}')





def MNpromedioDias(diccionario, variable, codigo_estacion, opcion):


    """
    Función que permite encontrar el valor promedio, mínimo y máximo de cierta variable en los
    últimos 7 o 30 días de una estación específica.

    Args:
        - diccionario (dict): Diccionario que contiene la información de las estaciones.
        - variable (str): Variable que se desea consultar.
        - codigo_estacion (str): Código de la estación que se desea consultar.
        - opcion (int): Opción que indica si se desea calcular los valores de los últimos 7 o 30 días.

    Returns:
        None. Imprime los valores promedio, máximo y mínimo de la variable en los últimos 7 o 30 días.

    """

    if opcion == 1:
        opcion = 7
    else:
        opcion = 30

    fechas = list(diccionario[codigo_estacion]['mediciones'].keys())
    fechas = fechas[-opcion:]

    valores = []
    for fecha in fechas:
        valor = diccionario[codigo_estacion]['mediciones'][fecha][variable]
        if valor != -999:
            valores.append(valor)

    
    if valores:
        promedio = sum(valores) / len(valores)
        minimo = valorMin(valores)
        maximo = valorMax(valores)
        print(f'El promedio de la variable {variable} en los últimos {opcion} días es {promedio}, el mínimo es {minimo} y el máximo es {maximo}.')
    else:
        print(f'No hay mediciones de la variable {variable} en los últimos {opcion} días en la estación con código {codigo_estacion}.')




def write_text(dic_usuarios,dic_estaciones,list_municipios,list_tipos_mediciones,mediciones):

    """
    Sinopsis:
        Función permite escribir la información en un archivo.txt siguiendo una estructura de manera estricta.


    Entradas y salidas:
    dic_usuarios: diccionario con los usuarios
    dic_estaciones: diccionario con las estaciones
    list_municipios: lista de municipios
    list_tipos_mediciones: listas con todos los tipos de variables
    mediciones: las mediciones estarán dentro de las estaciones, pero se ingresaran por separado.
    return: none

    """

    mUsuarios = []
    mMunicipios = []
    mEstacion = []
    mTMedida = ['PM10[0.0:100.0,ug/m3]', 'PM25[0.0:200.0,ug/m3]', 'Temperatura[-20.0:50.0,Â°C]', 'Humedad[0.0:100.0,%]']
    mMediciones = []
    mTMedicion = []
    Aux = ":"

    for clave, valor in dic_usuarios.items():
        usuarios = f"<{clave};{valor['usuario']};{valor['contrasena']};{valor['rol']}>"
        mUsuarios.append(usuarios)
        # print(clave,valor)

    for municipio in list_municipios:
        linea = f"{Aux}{municipio}"
        mMunicipios.append(linea)
        Aux = ","

    for clave,valor in dic_estaciones.items():
        estacion = f"{clave},{valor['nombre_estacion']},{valor['municipio']} "
        mEstacion.append(estacion)

    AuxWhile = 0
    while AuxWhile != len(list_tipos_mediciones)-1:
        linea = f"{list_tipos_mediciones[AuxWhile]},"
        mTMedicion.append(linea)
        AuxWhile += 1
    linea = f"{list_tipos_mediciones[AuxWhile]}"
    mTMedicion.append(linea)

    iterador = 0
    iteradorS = 0
    for medicion in mediciones:
        linea = f"{medicion[iteradorS]},{medicion[iteradorS+1]},{medicion[iteradorS+2]}"
        mMediciones.append(linea)
        iteradorS = 0



    # Escribir las líneas en un archivo de texto
    with open("datos.txt", "w") as archivo:

        for linea in mUsuarios:
            archivo.write(f"{linea}\n")
        archivo.write("\n")

        for linea in mMunicipios:
            archivo.write(f"{linea}")
        archivo.write("\n\n")    

        for linea in mEstacion:
            archivo.write(f"{linea}\n")
        archivo.write("\n")

        for linea in mTMedicion:
            archivo.write(f"{linea}")
        archivo.write("\n")
        archivo.write("\n")

        for linea in mMediciones:
            archivo.write(f"{linea}\n")
        archivo.write("\n")



