from funcionesPrincipales import *
from gestionUsuariosEstaciones import *
from utilidadesA import *
from validaciones import *

usuarios = {}
estaciones = {}
municipios = extraer_departamentos("registros_.txt")
variables = extraer_tipo_variable("registros_.txt")
lecturas = extraer_lecturas("registros_.txt")

extraer_estaciones("registros_.txt",estaciones)
extraer_usuarios("registros_.txt",usuarios)


for i in estaciones:
    print(estaciones[i])

# estaciones = {
#     '1': {
#         'nombre_estacion': 'giga',
#         'municipio': 'Medellín',
#         'mediciones': {
#             '2023-04-01': {'PM10': 20, 'PM25': 30, 'temperatura': 25, 'humedad': -999},
#             '2023-04-02': {'PM10': 25, 'PM25': 31, 'temperatura': -999, 'humedad': 20},
#             '2023-04-03': {'PM10': 31, 'PM25': 40, 'temperatura': 40, 'humedad': -999}
#         }
#     }


# }

# print(estaciones)

ejecucion = True

while ejecucion:
    extraer_usuarios("registros_.txt",usuarios)
    inicio_de_sesion(usuarios,estaciones)
    #Dicc , dicc , list , list , list
#Esto no se ejecuta ya que la funcion inicio_de_sesion fuerza el cierre de la ejecucion 
print("sali")
write_text(usuarios,estaciones,municipios,variables,lecturas)