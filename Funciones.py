import numpy as np
from Persona import *
def llenar(arreglo):
    x=0
    for f in range(10):
        for c in range(10):
            x = x + 1
            arreglo[f][c] = str(x)
def mostrar(arreglo):
    for f in range(10):
        fila = ''
        for c in range(10):
            fila = fila + ' ' + arreglo[f][c]
        print(fila)
def comprar(arreglo,num_asiento):
    num_asiento=comprobarasiento()
    x=1
    while(x<=num_asiento):
        print("Seleccione Ubicación: ")
        print("----------------------")
        mostrar(arreglo)
        print(f"Seleccione" , {x}, " asiento ")
        num_asiento = comprobarasiento()
        disponible = comprobarasiento(arreglo,num_asiento)
        if disponible==True:
            a=Persona()
            a.run=validar_rut()
            a.num_asiento=num_asiento
            a.valor=valor(num_asiento)
            print("Asiento comprado")
            x=x+1
            listarLosAsistentes.append(a)
        else:
            print("El asiento no se encuentra disponible")
def comprobarasiento(arreglo,num_asiento):
    x=0
    for f in range(10):
        for c in range(10):
            x=x+1
            if x==int(num_asiento):
                arreglo[f][c]='-X-'
                return False
            return True
def validar_rut():
    ciclo = True
    while(ciclo):
        run = input("Ingrese el RUN: ")
        if run.isnumeric() and len(run)==8:
            return run
        else:
            print("RUT invalido, debe ingresar los primeros 8 digitos del rut sin guión ni digito verificador")

def validar_asiento():
    ciclo = True
    while (ciclo):
        try:
            num_asiento = int(input("Ingrese numero de asiento (1-100)"))
            if num_asiento >=1 and num_asiento<=100:
                return num_asiento
            else:
                print("Numero de asiento invalido")
        except:
            print("Solo debe ingresar numeros")


def listarLosAsistentes(lista_asistentes):
    lista_asistentes.sort(key = lambda x: x.run)
    for a in lista_asistentes:
        print(f"RUT: {a.run} valor:{a.valor} Asiento: {a.num_asiento}")
def totales(lista_asistentes):
    p=0
    g=0
    s=0
    tot_p=0
    tot_g=0
    tot_s=0
    for asis in lista_asistentes:
        if int(asis.valor) == 120000:
            p=p+1
            tot_p=tot_p+120000
        if int(asis.valor) == 80000:
            g=g+1
            tot_g=tot_g+80000
        if int(asis.valor) == 50000:
            s=s+1
            tot_s=tot_s+50000
    print(f"Platinum: Cantidad:{p} Total:{tot_p}")
    print(f"Platinum: Cantidad:{g} Total:{tot_g}")
    print(f"Platinum: Cantidad:{s} Total:{tot_s}")

def agregarAsistentes(lista_asistentes,num_asiento):
    a = Persona()
    a.run=int(input("Ingrese su RUT: "))
    a.num_asiento = num_asiento
    if num_asiento>=1 and num_asiento<=20:
        a.valor=120000
    if num_asiento>=21 and num_asiento<=50:
        a.valor=80000
    if num_asiento>=51 and num_asiento<=100:
        a.valor=50000
    else:
        print("Ha escogido un número de asiento incorrecto, debe estar entre 1 y 100")
    lista_asistentes.append(a)

def comprarEntradas(arreglo,lista_asistentes):
    try:
        entradas = int(input("Ingrese Cantidad de entradas (1-3): "))
        if entradas>=1 and entradas<=3:
            comprar=0
            while comprar < entradas:
                mostrar(arreglo)
                num_asiento= int(input("Ingrese el numero de asiento: "))
                if num_asiento>=1 and num_asiento<=100:
                    disponible =  comprobarasiento(arreglo,num_asiento)
                    comprar(arreglo,num_asiento)
                    comprar = comprar + 1
                else:
                    print("El asiento no se encuentra disponible, seleccione otro")
        else:
            print("Ubicaciones entre 1 a 100")
    except BaseException as error:
        print(f"Error:{error}")
def valor(num_asiento):
    if int(num_asiento)>=1 and int(num_asiento)>=20:
        return 120000
    if int(num_asiento)>=21 and int(num_asiento)>=50:
        return 80000
    if int(num_asiento)>=51 and int(num_asiento)>=100:
        return 50000


#Reglas de negocio
#La cantidad de entradas fluctua entre 1 a 3 entradas
#Luego de elegir cantidad se desplega en pantalla las ubicaciones
#imprimir escenario
#Se debe desplegar un mensaje "No esta disponible"
#precios Platinum $120000 (asientos del 1 al 20)
#precios Gold $80.000 asientos del 21 al 50
#precios silver $50000 asientos del 51 al 100
#Registrar mensaje "La operación se ha realizado correctamente"
# En Ubicaciones disponibles misma imagen de op compra de entradas
#ver listado de asistentes: se debe ver por rut
#ganancias totales
