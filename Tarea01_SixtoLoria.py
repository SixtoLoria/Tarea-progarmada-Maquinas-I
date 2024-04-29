# =========================================================================================
#       Tarea 01
#       Estudiante: Sixto Alejandro Loria Villagra  C04417
#       Programa resolverdor de circuito magnetico.
# =========================================================================================

# NOTA: Es importante tener las librerias instaladas para el correcto funcionamiento.
# Usar: pip install pandas matplotlib sympy scipy numpy

# Librerias.
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from sympy import symbols, lambdify, sympify, exp
import numpy as np
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
# Banderas de ingreso de datos
Rel_I1 = False
Rel_I2 = False
Curva_act = False

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
    print("3) Calcular valores de la corriente y flujos laterales.")
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
            Rel_I1 = False
            Rel_I2 = False
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
                I1 = leer_numero("Ingrese el valor de la corriente 1 (En Amperes): ", "Flotante")
                F_ap = leer_apilado("Ingrese el valor del factor de apilado de las láminas(entre 0 y 1): ", "Flotante")
                
                SL = leer_numero("Ingrese el valor de SL(m^2): ", "Flotante")
                SC = leer_numero("Ingrese el valor de SC(m^2): ", "Flotante")
                A = leer_numero("Ingrese el valor del area (m^2): ", "Flotante")
                L1 = leer_numero("Ingrese el valor de L1(m): ", "Flotante")
                L2 = leer_numero("Ingrese el valor de L2(m): ", "Flotante")
                L3 = leer_numero("Ingrese el valor de L3(m): ", "Flotante")
                LE = leer_numero("Ingrese el valor de LE(m): ", "Flotante")
                Flujo_Deseado = leer_numero("Ingrese el valor del flujo deseado(Wb): ", "Flotante")
                
                Condicion_1 = False
                input("Regresando al menu principal Presione ENTER para continuar")
                                                                        
            elif Opcion_I == 2:
                # Solicitud de datos.
                Rel_I2 = True       # Para saber que tengo que resolver conociendo I2
                N1 = leer_numero("Ingrese el valor de vueltas de la bobina 1: ","Entero")
                N2 = leer_numero("Ingrese el valor de vueltas de la bobina 2: ","Entero")
                I2 = leer_numero("Ingrese el valor de la corriente en la bobina 2 (En Amperes): ", "Flotante")  
                F_ap = leer_apilado("Ingrese el valor del factor de apilado de las lámina (entre 0 y 1): ", "Flotante")

                SL = leer_numero("Ingrese el valor de SL(m^2): ", "Flotante")
                SC = leer_numero("Ingrese el valor de SC(m^2): ", "Flotante")
                A = leer_numero("Ingrese el valor del area (m^2): ", "Flotante")
                L1 = leer_numero("Ingrese el valor de L1(m): ", "Flotante")
                L2 = leer_numero("Ingrese el valor de L2(m): ", "Flotante")
                L3 = leer_numero("Ingrese el valor de L3(m): ", "Flotante")
                LE = leer_numero("Ingrese el valor de LE(m): ", "Flotante")
                Flujo_Deseado = leer_numero("Ingrese el valor del flujo por el entrehierro deseado(Wb): ", "Flotante")
                
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
            print("**                Seleccione como desea agregar la parametros de la curva            **")
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
                
                Agregar_pts = True
                while Agregar_pts:
                        H = leer_numero("Ingresa un valor de H : ", "Flotante")
                        B = leer_numero("Ingresa el valor de B correspondiente al H ingresado: ", "Flotante")
                        H_poins.append(H)      
                        B_poins.append(B)
                        Agregar_pts = validar_decision("Desea agregar mas valores(S/N)? ")                    
                #Creando funcion para interpolacion de datos
                f_curva = interp1d(H_poins, B_poins, kind='linear', fill_value='extrapolate')                 
                # Verificando que tengan la misma longitud
                if len(H_poins) != len(B_poins):
                    print("La cantidad de puntos ingresados para x no coincide con la cantidad de puntos ingresados para y.")     
                    print("Porfavor vuelva a ingresar los valores")
                    H_poins = []
                    B_poins = [] 
                else:
                    Curva_act = True # Bandera para saber si se ingreso una curva                 
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
                        
                    else:
                        # Salir de la opcion
                        print("Regresando")
                        
            elif Opcion_Cur == 2:
                # Solicitando valores de la ecuacion.
                Borrar_pantalla()
                print("***************************************************************************************")
                print("**                Ingrese la ecuacion de la curva de magnetizacion en forma          **")
                print("**                de strink, por ejemplo: a * H / (1 + b*H)                          **")
                print("**                                                                                   **")
                print("**     Donde: a y b son valores de la curva                                          **")
                print("***************************************************************************************\n")
                print()
                ecuacion = input("Ingrese la ecuación de la curva de magnetización: ")
                
                # Convertir la ecuación en una expresión simbólica
                H = symbols('H')
                expr = sympify(ecuacion)
                #expr = exp(H)
                # Crear una función a partir de la expresión
                func = lambdify(H, expr, 'numpy')
                # Generar datos para la gráfica
                H_vals = np.linspace(0, 5, 100)  # Ejemplo de valores para el eje H
                B_vals = func(H_vals)  # Calcular los valores correspondientes en M

                # Graficar la curva de magnetización
                plt.figure()
                plt.plot(H_vals, B_vals)
                plt.yscale('log')  # Escala logarítmica en el eje y
                plt.xlabel('H')
                plt.ylabel('B')
                plt.title('Curva de Magnetización')
                plt.grid(True)
                plt.show()

                # Devolver los datos de los ejes H y M en arreglos numpy
                H_poins = np.array(H_vals)
                B_poins = np.array(B_vals)
                Curva_act = True # Bandera para saber si se ingreso una curva
                f_curva = interp1d(H_poins, B_poins, kind='linear', fill_value='extrapolate')                  
            elif Opcion_Cur == 3:
               # Regresar al menu principal
                Condicion_2 = False       
            
    elif Opcion == 3:
        # Parte de calcular y mostrar resultados.
             
        if Rel_I1 == True and Curva_act == True:
            # Calculando valores     
            B3 = Flujo_Deseado / (SC * F_ap)
            H3 = f_curva(B3) # Se toma el valor correspondiente a la curva.
            #H3 = np.interp(B3, H_poins, B_poins) 
            L_fe = (L3 - LE)
            B_a = Flujo_Deseado / SC
            H_a = B_a / (4 * np.pi * 10 **(-7)) 
            F_mmAB = (H3 * L_fe + H_a * LE)
            
            # Se usa I1
            H1 = ((N1 * I1) - F_mmAB)/L1
            B1 = f_curva(H1) # Se toma el valor correspondiente a la curva.
            #B1 = np.interp(H1, H_poins, B_poins)
            # Calculando flujo 1
            Flujo_1 = B1 * SL * F_ap        
            # Calculando flujo 2
            Flujo_2 = Flujo_Deseado - Flujo_1
            
            # Calculando I2
            B2 = Flujo_2/(SL * F_ap)
            H2 = f_curva(B2) # Se toma el valor correspondiente a la curva.
            #H2 = np.interp(B2, H_poins, B_poins)
            
            I_2 = (H2 * L2 + F_mmAB)/N2 
            
            #Imprimiendo resultados.
            print(f"El valor del flujo por la columna 1 calculado es: {Flujo_1:.05} Wb")
            print(f"El valor del flujo por la columna 2 calculado es: {Flujo_2:.05} Wb")
            print(f"El valor de la corriente en la bobina 2 es: {I_2:.05} A")
            input("Presione Enter para continuar")
            
        elif Rel_I2 == True and Curva_act == True:
            # Calculando valores     
            B3 = Flujo_Deseado / (SC * F_ap)
            #H3 = f_curva(B3) # Se toma el valor correspondiente a la curva.
            H3 = np.interp(B3, H_poins, B_poins) 
            L_fe = (L3 - LE)
            B_a = Flujo_Deseado / SC
            H_a = B_a / (4 * np.pi * 10 **(-7)) 
            F_mmAB = (H3 * L_fe + H_a * LE)
            
            # Se usa I2
            H2 = ((N2 * I2) - F_mmAB)/L2
            #B2 = f_curva(H2) # Se toma el valor correspondiente a la curva.
            B2 = np.interp(H2, H_poins, B_poins)
            # Calculando flujo 2
            Flujo_2 = B2 * SL * F_ap        
            # Calculando flujo 1
            Flujo_1 = Flujo_Deseado - Flujo_2
            
            # Calculando I1
            B1 = Flujo_1/(SL * F_ap)
            #H1 = f_curva(B1) # Se toma el valor correspondiente a la curva.
            H1 = np.interp(B1, H_poins, B_poins)
            
            I_1 = (H1 * L1 + F_mmAB)/N1 
            
            #Imprimiendo resultados.
            print(f"El valor del flujo por la columna 1 calculado es: {Flujo_1:.05} Wb")
            print(f"El valor del flujo por la columna 2 calculado es: {Flujo_2:.05} Wb")
            print(f"El valor de la corriente en la bobina 2 es: {I_1:.05} A")
            input("Presione Enter para continuar")

        else:
            input("Primero se tienen que ingresar datos")
        
                    
    elif Opcion == 4:
        # El usuario desea terminar con el programa.
        Repetir = False
        
# Mensaje de salida.
print("Usted esta saliendo de la aplicacion...")
# Input para impedir cierre instantaneo de la aplicacion.
input("Presione ENTER para salir")