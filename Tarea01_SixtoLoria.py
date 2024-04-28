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


def leer_apilado(Mensaje, Tipo):
    """Esta funcion es para recibir numeros de apilado de laminado y validarlo"""
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
                Ev_lamin = True
                while Ev_lamin:
                    if Numero < 0 and Numero > 1:
                        print("ERROR, dato insertado no esta entre 0 y 1")
                    else:
                        Ev_lamin = False
                        return Numero
            else:
                # El usuario no inserto un numero
                print("ERROR, Estas usando mal la funcion")
        except ValueError:
            print("ERROR, dato insertado no es un numero")


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
    print("2) Ingresar y graficar curva de magnetizacion")
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
            # Restableciendo datos
            Rel_I1,Rel_I2 = False
            print("***************************************************************************************")
            print("**                  Ingrese cual valor de corriente conoce                           **")
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
                N1 = leer_numero("Ingrese el valor de vueltas de la bobina 1: ", "Entero")
                N2 = leer_numero("Ingrese el valor de vueltas de la bobina 2: ", "Entero")
                I1 = leer_numero("Ingrese el valor de la corriente 1 (En Ampers): ", "Flotante")
                Fa_laminas = leer_apilado("Ingrese el valor del factor de apilado de las lámina (entre 0 y 1): ", "Flotante")
                
                SL = leer_numero("Ingrese el valor de SL: ", "Flotante")
                SC = leer_numero("Ingrese el valor de SC: ", "Flotante")
                A = leer_numero("Ingrese el valor de; area (m^2): ", "Flotante")
                L1 = leer_numero("Ingrese el valor de L1: ", "Flotante")
                L2 = leer_numero("Ingrese el valor de L2: ", "Flotante")
                L3 = leer_numero("Ingrese el valor de L3: ", "Flotante")
                LE = leer_numero("Ingrese el valor de LE: ", "Flotante")
                Fluejo_Deseado = leer_numero("Ingrese el valor del flujo deseado: ", "Flotante")
                
                Ver_para = validar_decision("Desea ver los parametros ingresados (S/N)? ")
                
                if Ver_para == True:
                    print("Imprimir todo")
                    Condicion_1 = False
                    input("Presione ENTER para regresar")
                else:
                    # Regresando al menu con los datos registrados
                    Condicion_1 = False
                                                                    
            elif Opcion_I == 2:
                # Solicitud de datos.
                Rel_I2 = True       # Para saber que tengo que resolver conociendo I2
                N1 = leer_numero("Ingrese el valor de vueltas de la bobina 1: ","Entero")
                N2 = leer_numero("Ingrese el valor de vueltas de la bobina 2: ","Entero")
                I2 = leer_numero("Ingrese el valor de la corriente 2 (En Ampers): ", "Flotante")  
                Fa_laminas = leer_apilado("Ingrese el valor del factor de apilado de las lámina (entre 0 y 1): ", "Flotante")

                SL = leer_numero("Ingrese el valor de SL: ", "Flotante")
                SC = leer_numero("Ingrese el valor de SC: ", "Flotante")
                A = leer_numero("Ingrese el valor de; area (m^2): ", "Flotante")
                L1 = leer_numero("Ingrese el valor de L1: ", "Flotante")
                L2 = leer_numero("Ingrese el valor de L2: ", "Flotante")
                L3 = leer_numero("Ingrese el valor de L3: ", "Flotante")
                LE = leer_numero("Ingrese el valor de LE: ", "Flotante")
                Fluejo_Deseado = leer_numero("Ingrese el valor del flujo deseado: ", "Flotante")
                
                Condicion_1 = False
                input("Regresando al menu principal Presione ENTER para continuar")
            elif Opcion_I == 3:
                # Regresar al menu principal
                Condicion_1 = False         
                
    elif Opcion == 2:
        Condicion_2 = True
        while Condicion_2:
            # Borrando Pantalla
            Borrar_pantalla()
            print("***************************************************************************************")
            print("**                Ingrese como desearia agregar la parametros de la curva            **")
            print("***************************************************************************************\n")
            print("1) Ingresando valores de la curva")
            print("2) Ingresando la ecuacion de la curva")
            print("3) Regresar al menu principal")
        
            # Solicitar al usuario que seleccione una opcion
            Opcion_Cur = validar_opcion("Seleccione una opcion: ", (1, 2, 3))
            # Analizar la opcion selecionada
            
            if Opcion_Cur == 1:
                # Creando lista para guardar los puntos
                H_poins = [] # eje x
                B_poins = [] # eje y
                
                while True:
                    try:
                        H = input("Ingresa un valor de H (o cualquier caracter para finalizar): ")
                        if not H:
                            break
                        H = float(H)
                        B = float(input("Ingresa el valor de B correspondiente al H ingresado: "))
                        H_poins.append(H)      
                        B_poins.append(B)
                    except ValueError:
                        print("¡Debes ingresar un valor numérico para x e y!")  
                    # Verificando que tengan la misma longitud
                    if len(H_poins) != len(B_poins):
                       print("La cantidad de puntos ingresados para x no coincide con la cantidad de puntos ingresados para y.")     
                       print("Porfavor vuelva a ingresar los valores")
                       H_poins = []
                       B_poins = [] 
                    else:
                        
                        Ver_graf = validar_decision("Desea ver el grafico segun los datos ingresados (S/N)? ")   
                       
                        if Ver_graf == True:
                            # Crear gráfico de dispersión para B vs H
                            plt.plot(H_poins, B_poins)
                            # Configurar el gráfico
                            plt.xlabel('H (A/m)')
                            plt.ylabel('B (T)')
                            plt.title('Curva de magnetización')
                            plt.grid(True)
                            # Mostrar el gráfico
                            plt.show()
                            break
                        else:
                            # Salir de la opcion
                            break
                       
            elif Opcion_Cur == 2:
                print("Solicitar ecuacion")
                
            elif Opcion_Cur == 3:
               # Regresar al menu principal
                Condicion_2 = False       
            
            
                    
    elif Opcion == 4:
        # El usuario desea terminar con el programa.
        Repetir = False
        
# Mensaje de salida.
print("Usted esta saliendo de la aplicacion...")
# Input para impedir cierre instantaneo de la aplicacion.
input("Presione ENTER para salir")