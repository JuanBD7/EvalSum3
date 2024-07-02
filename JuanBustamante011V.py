#Prueba 3
import os
from random import *
os.system('cls')

lista_pedido=[]

def menu():
    print('Menu de opciones')
    print('1. Registrar pedido')
    print('2. Listar todos los pedidos')
    print('3. Imprimir Hoja de ruta')
    print('4. Salir')
    
def registrar_pedido():
    numero_pedido='1'
    print(numero_pedido)
    nombre=input('Ingrese nombre: ')
    apellido=input('Ingrese apellido: ')
    comuna=input('Ingrese comuna:San Bernardo/Calera de Tango/ Buin: ')
    direccion=input('Ingrese direccion: ')
    sacos_cinco=int(input('Seleccione cantidad de sacos de 5 kg: '))
    sacos_diez=int(input('Seleccione cantidad de sacos de 10 kg: '))
    sacos_veinte=int(input('Seleccione cantidad de sacos de 20 kg: '))
    
    diccionario={'Numero de pedido':numero_pedido,
                 'Nombre':nombre,
                 'Apellido':apellido,
                 'Direccion': direccion,
                 'Comuna':comuna,
                 'Sacos 5kg':(sacos_cinco),
                 'Sacos 10 kg':(sacos_diez),
                 'Sacos 20 kg': (sacos_veinte)}
    lista_pedido.append(diccionario)
    
    print('Registro exitoso')

def listar_pedidos():
        print(lista_pedido)
    
def imprimir_hoja_ruta():
    print('1. San Bernardo', '2. Calera de Tango', '3. Buin')
    sector=input('Seleccione un sector: ')
    if sector=='1':
        with open('hoja_ruta.txt', 'w') as archivo:
            archivo.write('Nro_Pedido  Nombre_Cliente        Apellido_Cliente      Direccion               Sector             Saco (5kg)   Saco (10kg)   Saco (20kg)')
            archivo.write('\n-------------------------------------------------------------------------------------------------------------------------------------------\n')
            for pedido in lista_pedido:
                nro_pedido=(pedido['Numero de pedido']).ljust(5)
                nombre_cliente=(pedido['Nombre']).ljust(15)
                apellido_cliente=(pedido['Apellido']).ljust(15)
                direccion_cliente=(pedido['Direccion']).ljust(20)
                sector_cliente=('San Bernardo').ljust(24)
                detalle_cliente_cinco=(pedido['Sacos 5kg']).rjust(15)
                detalle_cliente_diez=(pedido['Sacos 10 kg']).rjust(15)
                detalle_cliente_veinte=(pedido['Sacos 20 kg']).rjust(15)

                archivo.write(f'{nro_pedido}{nombre_cliente}{apellido_cliente}{direccion_cliente}{sector_cliente}{detalle_cliente_cinco}{detalle_cliente_diez}{detalle_cliente_veinte}')
        print('hoja_generada.txt')
    elif sector=='2':
        with open('hoja_ruta.txt', 'w') as archivo:
            archivo.write('Nro_Pedido  Nombre_Cliente        Apellido_Cliente      Direccion               Sector             Saco (5kg)   Saco (10kg)   Saco (20kg)')
            archivo.write('\n------------------------------------------------------------------------------------------------------------------------------------------\n')
            for pedido in lista_pedido:
                nro_pedido=(pedido['Numero de pedido']).ljust(12)
                nombre_cliente=(pedido['Nombre']).ljust(20)
                apellido_cliente=(pedido['Apellido']).ljust(22)
                direccion_cliente=(pedido['Direccion']).ljust(20)
                sector_cliente=('Calera de Tango').ljust(24)
                detalle_cliente_cinco=(pedido['Sacos 5kg']).rjust(15)
                detalle_cliente_diez=(pedido['Sacos 10 kg']).rjust(15)
                detalle_cliente_veinte=(pedido['Sacos 20 kg']).rjust(15)

                archivo.write(f'{nro_pedido}{nombre_cliente}{apellido_cliente}{direccion_cliente}{sector_cliente}{detalle_cliente_cinco}{detalle_cliente_diez}{detalle_cliente_veinte}')
        print('Hoja generada.txt')
    elif sector=='3':
        with open('hoja_ruta.txt', 'w') as archivo:
            archivo.write('Nro_Pedido  Nombre_Cliente        Apellido_Cliente      Direccion               Sector             Saco (5kg)   Saco (10kg)   Saco (20kg)')
            archivo.write('\n-------------------------------------------------------------------------------------------------------------------------------------------\n')
            for pedido in lista_pedido:
                nro_pedido=(pedido['Numero de pedido']).ljust(15)
                nombre_cliente=(pedido['Nombre']).ljust(15)
                apellido_cliente=(pedido['Apellido']).ljust(15)
                direccion_cliente=(pedido['Direccion']).ljust(20)
                sector_cliente=('Buin').ljust(15)
                detalle_cliente_cinco=(pedido['Sacos 5kg']).rjust(15)
                detalle_cliente_diez=(pedido['Sacos 10 kg']).rjust(15)
                detalle_cliente_veinte=(pedido['Sacos 20 kg']).rjust(15)

                archivo.write(f'{nro_pedido}{nombre_cliente}{apellido_cliente}{direccion_cliente}{sector_cliente}{detalle_cliente_cinco}{detalle_cliente_diez}{detalle_cliente_veinte}')
        print('Hoja generada.txt')
        
    return()
            

inicio=0
while inicio==0:
    try:
        menu()
        opcion=int(input('Ingresa una opcion: '))
        if opcion==1:
            registrar_pedido()
            pregunta=input('¿Desea hacer otra operacion?  si= 1 / no= 2: ')
            if pregunta=='1':
                inicio=0
            elif pregunta=='2':
                print('Ok, muchas gracias')
                inicio=1
        elif opcion==2:
            listar_pedidos()
        elif opcion==3:
            imprimir_hoja_ruta()
            inicio=1
        elif opcion==4:
            print('Haz salido del programa')
            inicio=1
    except ValueError:
        print('Numero mal Ingresado')


