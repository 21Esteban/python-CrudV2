def valorMin(lista):

    """
    Sinopsis:
        Función permite encontrar el valor minimo en una lista de números


    Entradas y salidas:
        lista: lista de números
        minimo: valor minimo encontrado

    """

    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo

def valorMax(lista):

    """
    Sinopsis:
        Función permite encontrar el valor maximo en una lista de números


    Entradas y salidas:
        lista: lista de números
        máximo: valor mayor encontrado

    """

    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

def sleep(nSegundos):

    """
    Sinopsis:
        Función permite simular el pausado de la ejecución del código


    Entradas y salidas:
        nSegundos: segundos en los que se pausará el codigo
        returns: none

    """

    from datetime import datetime
    tiempo_inicio = datetime.now()
    while (datetime.now() - tiempo_inicio).total_seconds() < nSegundos:
        pass

def sumList(lista):

    """
    Sinopsis:
        Función permite calcular la suma de todos los elementos de una lista


    Entradas y salidas:
        - lista: lista base que contiene los datos
        - returns: suma

    """

    suma = 0
    for i in lista:
        suma += i
    return suma

def clean_screen():
    import sys
    import os
    """
    Sinopsis:
        Función que permite limpiar la pantalla


    Entradas y salidas:
        - returns: none, solo se limpia la pantalla
    """

    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        print("\033c", end="")

def open_file(archivo):

    """
    Sinopsis:
        funcion que permite abrir un archivo dado como argumento y cargarlo en memoria

    Entradas y salidas:
        - archivo: nombre del archivo
        - returns: lineas 
    """

    with open(archivo,encoding='utf-8') as file:
        lineas = file.readlines()
        return lineas
    
def posLineWhite(archivo):

    """
    Sinopsis:
        funcion que permite calcular la posición de las lineas que está completamente en blanco de un archivo

    Entradas y salidas:
        - archivo: nombre del archivo
        - returns: posLineWhite 
    """

    lectura = open_file(archivo) 
    posLineWhite = []
    pos = 0

    for linea in lectura:
        linea_limpia = linea.rstrip()
        if len(linea_limpia) == 0:
            posLineWhite.append(pos)
        pos += 1

    return posLineWhite

def search_position(linea, separadores):

    """
    Sinopsis:
        funcion que nos permite encontrar las ubicación exacta de los separadores en el string ingresado

    Entradas y salidas:
        - linea: string a evaluar
        - separadores: delimitador a buscar
        - returns: pos: posiciones
    """

    pos = []
    posi = 0
    for caracter in linea:
        posi += 1
        if caracter in separadores:
            pos.append(posi-1)
    return pos

def custom_split(string,separadores):
    
    """
    Sinopsis:
        funcion que nos permite encontrar las ubicación exacta de los separadores en el string ingresado

    Entradas y salidas:
        - linea: string a evaluar
        - separadores: delimitador a buscar
        - returns: pos: posiciones

    """

    pos = search_position(string, separadores)
    list_elementos = []

    # Verificar si el primer elemento no tiene separador antes de él
    if pos[0] != 0:
        list_elementos.append(string[:pos[0]])
        
    # Iterar por los separadores encontrados para obtener los elementos
    for i in range(len(pos) - 1):
        indice0 = pos[i] + 1
        indice1 = pos[i+1]
        list_elementos.append(string[indice0:indice1])
    # Agregar el último elemento
    indice0 = pos[-1] + 1
    list_elementos.append(string[indice0:])
    return list_elementos

def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
    '''
    def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        se: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)
        
    def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        # Imprimir celda
        if type(texto) == type(0.0):
            #print(texto)
            texto = '{:^7.2f}'.format(texto)
            #print(type(texto), texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
    def imprimir_fila(fila):
        '''
        fila: Lista con los textos de las celdas de la fila
        '''
        impresos = []   
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto)//(ancho[i]-4)
            if len(texto)%(ancho[i]-4) != 0:
                alto1+=1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            print('| ',end='')
            for j in range(len(fila)):
                relleno = ancho[j]-3
                if j == len(fila)-1:
                    relleno = ancho[j] -4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' |')
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' | ',end='')   
    if not len(tabla) > 0:
        return
    if not type(tabla[0]) is list:
        return
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho+3]*ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i]+=3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado != None:
        dividir_fila(ancho,'=')
        imprimir_fila(encabezado)
        dividir_fila(ancho,'=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)

def opciones_validas(diccionario):
    string = ""
    for i in diccionario:
        string += str(i)
    last_p = int(i) + 1 
    string += str(last_p)
    return string