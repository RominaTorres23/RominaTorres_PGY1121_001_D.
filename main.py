import numpy as np
from Funciones import *
from Persona import *

arreglo = np.full([10,10],'---')
lista_asistentes = []
ciclo = True
llenar=arreglo

def salir():
    print("Ha salido del sistema, atentamente Romina Torres Candia, 06 de Julio de 2023")
    return False

while(ciclo):
    print("PRODUCTORA DE EVENTOS CREATIVOS.CL")
    print("----------------------------------")
    print("1) Comprar Entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver listado de asistentes")
    print("4) Mostrar Ganancias Totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione (1-5): "))
        match op:
            case 1:
                comprarEntradas(arreglo,lista_asistentes)
            case 2:
                mostrar(arreglo)
            case 3:
                listarLosAsistentes(lista_asistentes)
            case 4:
                totales(lista_asistentes)
            case 5:
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")




