def validar_fecha(fecha):
    """
    Sinopsis:
        Función que permite validar si una fecha está en el formato dado


    Entradas y salidas:
        - fecha: fecha que será validada
        - returns: True o False dependiendo de si es valida
    """
    
    import datetime
    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validacion_rango(valor, minimo, maximo):

    """
    Sinopsis:
        Función que permite validar si un número está en un rango dado


    Entradas y salidas:
        - valor: valor para hacer la comprobación
        - minimo: valor minimo del rango
        - maximo: valor maximo del rango
        - returns: True o False dependiendo de si es valido o no
    """

    if valor >= minimo and valor <= maximo or valor == "ND":
        return True
    else:
        return False
    
def validar_existencia(documento,diccionario):

    """
    Sinopsis:
        Función que comprueba la existencia de una clave en un diccionario 

    Entradas y salidas:
        - documento: documento que se buscará en la base de datos
        - diccionario: diciconario donde se buscará el documento 
        - returns: num
    """

    for clave in diccionario:
        if documento in clave:
            return True
    return False

def validar_identificacion(documento):

    """
    Sinopsis:
        Función que permite validar si un documento de identidad tiene únicamente 10 digitos.


    Entradas y salidas:
        - documento: documento de identidad en str
        - returns: True o False dependiendo de si es valido
    """

    contDigitos = 0
    digitos = "0123456789"

    while contDigitos != 10:
        #contDigitos = 0
        for d in documento:
            if d in digitos:
                contDigitos += 1
            
            if contDigitos != 10 and len(documento) != 10 or d not in digitos:
                return False
    return True

def validar_nombre_usuario(nombre):
    
    """
    Sinopsis:
        Función que permite validar si un nombre de usuario es valido, es decir que solo tenga 
        letras y espacios.


    Entradas y salidas:
        - nombre: nombre de usuario ingresado por el usuario
        - returns: True o False dependiendo de si es valido
    """

    nombre = nombre.lower()
    cont = 1
    cInvalidos = "0123456789!@#\$%\^&\*\(\)_\+-=\[\]{}\\\|;':\",.<>\?\/"
    while cont != 0:
        for caracter in nombre:
            if caracter in cInvalidos:
                return False
        return True
    
def validar_password(password):

    """
    Sinopsis:
        Función que permite validar si una contraseña de usuario es valida, es decir que tenga
        minimo 4 digitos. 


    Entradas y salidas:
        - password: contraseña ingresada como argumento
        - returns: True o False dependiendo de si es valida
    """

    longitud = len(password)
    if longitud < 4:
        return False
    else:
        return True