# =========================================================================================
#       Tarea 01
#       Estudiante: Sixto Alejandro Loria Villagra  C04417
#       Programa resolverdor de circuito magnetico.
# =========================================================================================

# Librerias.
import pandas as pd
import matplotlib.pyplot as plt
import os

# BORRAR PANTALLA.f
Borrar_pantalla = lambda: os.system("cls")


# ----------------------- Funciones ------------------------------

def leer_numero(Mensaje, Tipo):
    """Esta funcion es para recibir numeros del usuario y validarlos"""
    while True:
        # Solicitando un entero del teclado
        Numero =  input(Mensaje)
        # validacion
        try:
            if Tipo == "Entero":
                #Transformando numero a entero
                Numero = int(Numero)
                # Salida del cliclo while
                return Numero
            elif Tipo == "Flotante":
                # Convertir numero a flotante
                Numero = float(Numero)
                return Numero
            else:
                # El usuario no inserto un numero
                print("ERROR, dato insertado no es un numero")
        except ValueError:
            print("ERROR, dato insertado no es un numero")
    # Retornando el numero validado al programa
    return Numero

def validar_opcion(Mensaje, Opciones):
    """Solicitarle al usuario que seleccione una opicion valida"""
    # Ciclo de validacion
    while True:
        # solicitar el usuario que seleccione una de las opciones
        Opcion = leer_numero(Mensaje, "Entero")
        # Necesitamos saber cuantas opciones hay en la lista
        Num_Op = len(Opciones)
        # Validar la opcion
        for Indice in range(Num_Op):
            # Verificar si opcion esta en la lista
            if Opcion == Opciones[Indice]:
                # Opcion valida
                return Opcion
        # si Salimos del ciclo for sin que hubiera coincidencia
        print("ERROR, el dato insertado no esta entre las opciones")
        
        
def validar_decision(Mensaje):
    """Esta funcion valida si el usuario desea aceptar una opcion seleccionada"""
    # Creando condicion de validacion
    Condicion = True
    # Ciclo wihle de repetcion
    while Condicion:
        # Preguntar al usuario si desea repetir la opcion
        Letra = input(Mensaje)
        # Validar la Opcion seleccionada
        if Letra == "S" or Letra == "s":
            # Usuario desea repetir
            return True
        elif Letra == "N" or Letra == "n":
            # Usuario quiere salir
            return False
        else:
            # opcion seleccionada es invalida
            print("ERROR:, La opcion seleccionada es invalida")
            
            
# =================================================================
#                    Programa Principal
# =================================================================

# Ciclo de repeticion
Repetir = True
# Ciclo principal
while Repetir:
    # Borrando pantalla
    Borrar_pantalla()
    # Mostrando el menu principal
    print("***************************************************************************************")
    print("**                                                                                   **")
    print("**       PROGRAMA QUE RESUELVE UN CIRCUITO MAGNETICO A PARTIR DE PARAMETROS          **")
    print("**                                                                                   **")
    print("***************************************************************************************\n")

    print("MENU PRINCIPAL: ")
    print()
    print("1) Insertar parametros del circuito")
    print("2) Graficar curva de magnetizacion")
    print("3) Calcular valores de las corrientes.")
    print("4) Salir del programa")
    # Solicitar al usuario que seleccione una opcion
    Opcion = validar_opcion("Seleccione una opcion: ", (1, 2, 3, 4))
    # Analizar la opcion selecionada
    if Opcion == 1: #-------------------------------------------------------------
        Condicion_1 = True
        while Condicion_1:
            # Borrando Pantalla
            Borrar_pantalla()
            print("***************************************************************************************")
            print("**                  Ingrese cual valor de corriente conoce                          **")
            print("***************************************************************************************\n")
            print("1) Corriente en la bobina 1 (I1)")
            print("2) Corriente en la bobina 2 (I2)")
            print("3) Regresar al menu principal")
        
            # Solicitar al usuario que seleccione una opcion
            Opcion_I = validar_opcion("Seleccione una opcion: ", (1, 2, 3))
            # Analizar la opcion selecionada

            if Opcion_I == 1:
                
                # Solicitud de datos.
                Rel_I1 = True       # Para saber que tengo que resolver conociendo I1
                N1 = leer_numero("Ingrese el valor de vueltas de la bobina 1: ","Entero")
                N2 = leer_numero("Ingrese el valor de vueltas de la bobina 2: ","Entero")
                I1 = leer_numero("Ingrese el valor de la corriente 1 (En Ampers): ", "Flotante")
        
            
            
    else:
        print("Salir")