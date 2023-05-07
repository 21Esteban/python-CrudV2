from utilidadesA import *
from funcionesPrincipales import *
from validaciones import *

def identificacion():
    
    """
    Sinopsis:
        Función que le solicita al usuario que ingrese un documento de identidad y valida si cumple 
        con los requerimientos.


    Entradas y salidas:
        - None
        - returns: documento 
    """

    documento = " "
    while validar_identificacion(documento) != True:
        documento = input("Ingrese documento de identidad del usuario: ")
        if validar_identificacion(documento) != True:
            print("Ingrese un documento valido")

    return documento 

def nombre_usuario():

    """
    Sinopsis:
        Función que le solicita al usuario el nombre de usuario para la plataforma y valida 
        si es valido, es decir que solo tenga letras y espacios, por otra parte convierte las
        mayusculas a minusculas.


    Entradas y salidas:
        - None
        - returns: nombre_usuario
    """

    nombreU = "1"
    while validar_nombre_usuario(nombreU) != True:
        nombreU = input("Ingrese el nombre de usuario: ").lower()
        if validar_nombre_usuario(nombreU) != True:
            print("El nombre de usuario solo puede contener letras y espacios, intenta nuevamente.")
    return nombreU 

def password(modo):

    """
    Sinopsis:
        Funcion que le solicita al usuario que ingrese una contraseña, verifica 
        si es valida y la retorna; por otra parte tiene dos modos:
        1. Para escribir la contraseña una sola vez
        2. Para escribir la contraseña y confirmarla


    Entradas y salidas:
        - modo: 1 o 2 dependiendo de lo que se requiera
        - returns: passwordA
    """

    passwordA = ""

    if modo == 1:
        while validar_password(passwordA) != True:
            passwordA = input("Ingrese la contraseña: ")
            if validar_password(passwordA) != True:
                print("Ingrese una contraseña de minimo 4 caracteres")

    elif modo == 2:
        comprobacion = False
        while validar_password(passwordA) != True or comprobacion != True:
            passwordA = input("Ingrese la contraseña: ")
            if validar_password(passwordA) != True:
                print("Ingrese una contraseña de minimo 4 caracteres")
            else:
                passwordB = input("Confirme su contraseña: ")
                if passwordA == passwordB:
                    comprobacion = True
                else:
                    print("Las credenciales son diferentes, ingrese la contraseña y confirme nuevamente")
    return passwordA

def crear_usuario(diccionario,estaciones):

    """
    Sinopsis:
        Función que hace uso de otras funciones creadas anteriormente y recopila el documento de 
        identificación, contraseña y rol para después retornar un diccionario agregando esta 
        información.


    Entradas y salidas:
        - diccionario: diccionario que se usará como base para consultar la existencia de documentos y 
        se actualizará con los nuevos usuarios. 
        - returns: none solo se hacen las ediciones correspondientes
    """

    ID = list(diccionario.keys())[0]
    while validar_existencia(ID, diccionario):
        ID = identificacion()
        if validar_existencia(ID, diccionario):
            print("Este documento de identidad ya está registrado en la base de datos")

    user = nombre_usuario()
    contrasena = password(2)
    rol = respuesta_numerica("Seleccione el rol 1. Admin y 2. Operador:","12")

    if rol == "2":
        diccionario[ID] = {'usuario': user, 'contrasena': contrasena, 'rol': 'Operador'}
    elif rol == "1":
        diccionario[ID] = {'usuario': user, 'contrasena': contrasena, 'rol': 'Administrador'}
    print("El usuario se ha creado con exito")
    sleep(2)
    clean_screen()
    AccionesAdmin(diccionario,estaciones)

def editar_usuario(diccionario,estaciones):

    """
    Sinopsis:
        Función que hace uso de otras funciones creadas anteriormente, permite editar usuarios existentes
        en un diccionario


    Entradas y salidas:
        - diccionario: diccionario que se usará como base para consultar la existencia de documentos y 
        edición de usuarios 
        - returns: none solo se hacen las ediciones correspondientes
    """

    print("Los usuarios existentes son: ")
    for documento in diccionario:
        #print(documento)
        print(documento, diccionario[documento]["usuario"])

    validar = False
    while validar != True:
        print("Escriba el documento de identidad del usuario que desea editar: ")
        user = identificacion()
        validar = validar_existencia(user,diccionario)
        if validar == False:
            print("Ingrese un usuario existente")
    
    print("El nombre de usuario actual es:", diccionario[user]["usuario"], ", se le solicitará uno nuevo.")
    nuevo_nombre = nombre_usuario()
    diccionario[user]["usuario"] = nuevo_nombre
    print("La contraseña de usuario actual es:", diccionario[user]["contrasena"], ", se le solicitará una nueva.")
    nueva_password = password(2)
    diccionario[user]["contrasena"] = nueva_password
    print("El rol del usuario actual es:", diccionario[user]["rol"], ", se le solicitará uno nuevo.")
    nuevo_rol = respuesta_numerica("Seleccione el rol 1. Admin y 2. Operador:","12")
    if nuevo_rol == "2": 
        diccionario[user]["rol"] = "Operador"
    elif nuevo_rol == "1":
        diccionario[user]["rol"] = "Administrador"
        
    sleep(2)
    clean_screen()
    AccionesAdmin(diccionario,estaciones)

def eliminar_usuario(diccionario,estaciones):
    
    """
    Sinopsis:
        Función que hace uso de otras funciones creadas anteriormente permite eliminar usuarios
        de un diccionario.


    Entradas y salidas:
        - diccionario: diccionario que se usará como base para consultar la existencia de documentos 
        y eliminar usuarios.
        - returns: none solo se hacen las eliminaciones correspondientes
    """

    print("Los usuarios existentes son: ")
    for documento in diccionario:
        print(documento, diccionario[documento]["usuario"])
              
    validar = False
    while validar != True:
        user = input("Escriba el documento de identidad del usuario que desea eliminar: ")
        validar = validar_existencia(user,diccionario)
        if validar == False:
            print("Ingrese un usuario existente")
    
    del diccionario[user]
    print("El usuario se ha eliminado con éxito")
    sleep(2)
    clean_screen()
    AccionesAdmin(diccionario,estaciones)

#  Funciones para las estaciones

def crear_estacion(diccionario):

    """
    Sinopsis:
        funcion que usa el diccionario y crea una nueva estación dentro en base
        a la información ingresada por el usuario.


    Entradas y salidas:
        - diccionario: diccionario de estaciones
        - returns: none, y la actualización del diccionario tomado como paramétro 
        con la información de la nueva estación. 
    """

    municipios = ["Medellín","Bello","Itagui","Caldas","La Estrella","Barbosa"]
    nombre_estacion = input("Ingrese el nombre de la estacion, (Es valido cualquier caracter):")
    codigo = generar_codigo(diccionario)
    print("--------------------------")
    indice = 1
    for i in municipios:
        print(i, "("+str(indice)+")" )
        indice += 1
    print("--------------------------")    
    modo = respuesta_numerica("Seleccione uno de los municipios disponibles:\n","123456")
    modo = int(modo)

    diccionario[codigo] = {'nombre_estacion': nombre_estacion, 'municipio': municipios[modo-1], "mediciones": {} }

    





def editar_estacion(diccionario):
    
    """
    Sinopsis:
        funcion que usa el diccionario y nos permite editar la información 
        de alguna de las estaciones 


    Entradas y salidas:
        - diccionario: diccionario de estaciones
        - returns: none, y la actualización del diccionario con la nueva 
        información. 
    """

    municipios = ["Medellín","Bello","Itagui","Caldas","La Estrella","Barbosa"]
    print("Los códigos de las estaciones existentes son: ")
    for estacion in diccionario:
        print(estacion, diccionario[estacion]["nombre_estacion"])
    
    validar = False
    while validar != True:
        codigo = input("Escriba el código de la estacion que desea editar:")
        validar = validar_existencia(codigo,diccionario)
        if validar == False:
            print("Ingrese un codigo de estación existente")

    print("El nombre de la estación es:", diccionario[codigo]["nombre_estacion"], ", se le solicitará uno nuevo.")
    nnombre_estacion = input("Ingrese el nombre de la estacion, (Es valido cualquier caracter):")
    diccionario[codigo]["nombre_estacion"] = nnombre_estacion
    print("El municipio actual es:", diccionario[codigo]["municipio"], ", se le solicitará uno nuevo.\n")

    indice = 1
    for i in municipios:
        print(i, "("+str(indice)+")" )
        indice += 1
    print("--------------------------")    
    modo = respuesta_numerica("Seleccione uno de los municipios disponibles:\n","123456")
    modo = int(modo)

def eliminar_estacion(diccionario):

    """
    Sinopsis:
        funcion que usa el diccionario y nos permite editar una estación existente.

    Entradas y salidas:
        - diccionario: diccionario de estaciones
        - returns: none, y la actualización del diccionario. 
    """

    print("Las estaciones existentes son: ")
    for codigo in diccionario:
        print(codigo, diccionario[codigo]["nombre_estacion"])

    validar = False
    while validar != True:
        codigo = input("Escriba el codigo de la estacion que desea eliminar: ")
        validar = validar_existencia(codigo,diccionario)
        if validar == False:
            print("Ingrese un codigo de estacíón valido")

    del diccionario[codigo]

#############################################################################
usuarios = {}
estaciones = {}
municipios = extraer_departamentos("registros_.txt")
variables = extraer_tipo_variable("registros_.txt")
lecturas = extraer_lecturas("registros_.txt")
extraer_estaciones("registros_.txt",estaciones)
extraer_usuarios("registros_.txt",usuarios)


def inicio_de_sesion(usuarios,estaciones):

    """
    Sinopsis:
        Función que permite simula un inicio de sesion en una plataforma en base al documento de identidad
        ,nombre de usuario y contraseña.


    Entradas y salidas:
        - diccionario: diccionario base que contiene la información
        - returns: none
        - Si se autoriza el ingreso, se redirige la ejecución a otra funcion

    """
    # clean_screen()
    print("Bienvenido a la Gestion de Variables Ambientales V1.2")
    mode = respuesta_numerica("Seleccione: \n""1.Usuario Registrado\n""2.Usuario Visitante\n""3.Finalizar Ejecución\n","123")
    
    if mode == "1":
        ID = identificacion()
        comprobacion = validar_existencia(ID,usuarios)
        if comprobacion:
            print("El documento se ha encontrado en la base de datos")
            contrasena = password(1)
            if usuarios[ID]['contrasena'] == contrasena:
                usuario = usuarios[ID]["usuario"]
                print(f"Has iniciado sesion exitosamente {usuario}")
                sleep(2)
                clean_screen()

                if usuarios[ID]["rol"] == "Administrador":
                    print("Tu rol es Administrador")
                    AccionesAdmin(usuarios,estaciones)

                elif usuarios[ID]["rol"] == "Operador":
                    print("Tu rol es Operador")
            else:
                print("Nombre de usuario errado")
                sleep(2)
                clean_screen()
        else:
            print("El documento no se ha encontrado en la base de datos")
            sleep(2)

            
    elif mode == "2":
        print("Cargando Opciones............")
        sleep(2)
        clean_screen()
        VisualizarEstadisticas(usuarios,estaciones)

    elif mode == "3":
        write_text(usuarios,estaciones,municipios,variables,lecturas)
        exit()

###########################################################################################

def VisualizarEstadisticas(diccionario,estaciones):

    """
    Función que permite visualizar las estadisticas de cierta variable

    Entradas y salidas
        - estaciones (dict): Diccionario que contiene la información de las estaciones

    Returns:
        None. Imprime la información solicitada por el usuario

    """

    clean_screen()
    print("Seleccione el código de una de las siguientes estaciones:\n ")
    for i in estaciones:
        estacion = estaciones[i]["nombre_estacion"]
        print(i,estacion)
    print("--------------------------")

    nDis = opciones_validas(estaciones)
    estacion = respuesta_numerica("Seleccione la Estacion: ",nDis)

    opciones = \
           "Escoja La Variable que desea visualizar\n"\
           "1. PM10\n" \
           "2. PM25\n" \
           "3. Temperatura\n" \
           "4. Humedad\n" \
           "--------------------------\n"
    
    modo = respuesta_numerica(opciones,"1234")

    opciones = \
           "Escoja el tipo de Analisis\n"\
           "1. Últimos 7 días\n" \
           "2. Últimos 30 días\n" \
           "3. Fecha Especifica\n" \
           "--------------------------\n"
    
    modoEstadistica = respuesta_numerica(opciones, "123")

    if modoEstadistica == "1":
        if modo == "1":
            MNpromedioDias(estaciones, "PM10", estacion,1)
        elif modo == "2":
            MNpromedioDias(estaciones, "PM25", estacion,1)
        elif modo == "3":
            MNpromedioDias(estaciones, "temperatura", estacion,1)
        elif modo == "4":
            MNpromedioDias(estaciones, "humedad", estacion,1)

    elif modoEstadistica == "2":
        if modo == "1":
            MNpromedioDias(estaciones, "PM10", estacion,2)
        elif modo == "2":
            MNpromedioDias(estaciones, "PM25", estacion,2)
        elif modo == "3":
            MNpromedioDias(estaciones, "temperatura", estacion,2)
        elif modo == "4":
            MNpromedioDias(estaciones, "humedad", estacion,2)

    elif modoEstadistica == "3":
        if modo == "1":
            fecha = solicitar_fecha()
            MedicionFechaEspecifica(estaciones, "PM10", fecha,estacion)
        elif modo == "2":
            fecha = solicitar_fecha()
            MedicionFechaEspecifica(estaciones, "PM25", fecha,estacion)
        elif modo == "3":
            fecha = solicitar_fecha()
            MedicionFechaEspecifica(estaciones, "temperatura", fecha,estacion)
        elif modo == "4":
            fecha = solicitar_fecha()
            MedicionFechaEspecifica(estaciones, "humedad", fecha,estacion)

    sleep(5)
    clean_screen()
    AccionesAdmin(diccionario,estaciones)

def AccionesAdmin(usuarios,estaciones):

    print("Como usuario administrador puedes realizar las siguientes acciones:")

    opciones = \
           "1. Crear Usuario\n" \
           "2. Eliminar Usuario\n" \
           "3. Editar Usuario\n" \
           "4. Crear Estación\n" \
           "5. Editar Estación\n" \
           "6. Eliminar Estación\n" \
           "7. Visualizar Estadisticas\n"\
           "8. Retroceder\n"\
           "9. Finalizar Ejecución\n"\
           "--------------------------\n"
    
    modo = respuesta_numerica(opciones,"123456789")

    if modo == "1":
        crear_usuario(usuarios,estaciones)
    elif modo == "2":
        eliminar_usuario(usuarios,estaciones)
    elif modo == "3":
        editar_usuario(usuarios,estaciones)
    elif modo == "4":
        crear_estacion(estaciones)
    elif modo == "5":
        editar_estacion(estaciones)
    elif modo == "6":
        eliminar_estacion(estaciones)
    elif modo == "7":
        VisualizarEstadisticas(usuarios,estaciones)
    elif modo == "8":
        inicio_de_sesion(usuarios,estaciones)
        pass
    elif modo == "9":
        exit()