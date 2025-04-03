import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Funcion_externa.funcion_secundaria import main
from menus import media
from FaltaPromedio import tP
def reprobadas():
    while True:
        try:
            semestre = int(input("¿Qué semestre cursas actualmente?: "))
            if 0 <= semestre <= 11:
                break
            else:
                print("No puedes estar en 11 semestre, se realista rey")
        except ValueError:
            print("Ingresa una opción válida.")
            print("Ingresa un número válido para el semestre.")
    
    while True:  
        try:
            na = int(input("Escribe cuántas materias reprobadas tienes: "))
            if na < 0:
                print("El número de materias reprobadas no puede ser negativo.")
            elif na > 15:
                print("Nombre mijo no puedes tener ese número de reprobadas.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    if semestre <= 2 and na == 0:
        print("¡Excelente! Vas empezando y no tienes materias reprobadas.")
    elif semestre <= 2 and 1 <= na <= 3:
        print("Cuidado, estás empezando y ya tienes algunas materias reprobadas.")
    elif semestre <= 2 and na > 3:
        print("Es preocupante tener tantas materias reprobadas al inicio. ¡Habla con tu tutor!")
    elif 3 <= semestre <= 5 and na == 0:
        print("¡Muy bien! Vas a la mitad de la carrera y sin materias reprobadas.")
    elif 3 <= semestre <= 5 and 1 <= na <= 4:
        print("Vas a la mitad de la carrera, pero necesitas mejorar para evitar problemas.")
    elif 3 <= semestre <= 5 and 5 <= na <= 7:
        print("No manches carnal, andas peligrando algo eh, ponle ganitas.")
    elif 3 <= semestre <= 5 and na > 7:
        print("Tienes muchas materias reprobadas. Considera buscar ayuda académica.")
    elif 6 <= semestre <= 7 and na == 0:
        print("¡Felicidades! Estás por terminar y no tienes materias reprobadas.")
    elif 6 <= semestre <= 7 and 1 <= na <= 4:
        print("Dale calma, pero tampoco te relajes mucho.")
    elif 6 <= semestre <= 7 and 5 <= na <= 8:
        print("Ey ve cuidando tus N/A, no bajes la guardia.")
    elif 6 <= semestre <= 7 and 9 <= na <= 10:
        print("Compa, ya ponle esfuerzo, estás peligrando bastante de ser dado de baja.")
    elif 6 <= semestre <= 7 and na > 10:
        print("Tan cercas, le hubieras echado ganas compa.")
    elif semestre >= 8 and na == 0:
        print("¡Increíble! Estás por graduarte y no tienes materias reprobadas.")
    elif semestre >= 8 and 1 <= na <= 3:
        print("Estás por terminar, pero necesitas enfocarte para no acumular más reprobadas.")
    elif semestre >= 8 and 4 <= na <= 6:
        print("Cuidado, estás en la recta final y tienes varias materias reprobadas.")
    elif semestre >= 8 and na > 6:
        print("Es preocupante tener tantas materias reprobadas al final. ¡Busca apoyo académico!")
    else:
        print("No se pudo determinar un caso específico. Revisa tus datos.")
def menu():
    while True:
        try:
            print("Bienvenido al programa donde vas a poder consultar distintas cosas acerca de tu semestre de la universidad en la UACH") 
            print("A continuación se muestran las opciones a las que puede acceder: ")
            print("Opción 1: Promedio de tus calificaciones de todo el semestre:")
            print("Opción 2: Tus asistencias a clases durante el semestre")
            print("Opción 3: Riesgo que tienes de ser dado de baja por tus No Acreditadas")
            print("Opción 4: Cuánto te falta para aprobar el semestre, considerando la calificación mínima como 7")
            print("Opción 5: Salir")
            opcion = int(input("Digita la opción que deseas seleccionar hoy: "))
            match opcion:
                case 1:
                    media()
                    while True:  
                        continuar = input("\n¡Deseas hacer algo más? (s/n): ").lower().strip()
                        if continuar in ["s", "si", "n", "no"]:
                            break  
                        print("Por favor, ingresa 's' para continuar o 'n' para salir.")
                    if continuar in ["n", "no"]:  
                        print("Gracias por usar el programa!!!")
                        break
                case 2:
                    main()
                    while True:  
                        continuar = input("\n¡Deseas hacer algo más? (s/n): ").lower().strip()
                        if continuar in ["s", "si", "n", "no"]:
                            break  
                        print("Por favor, ingresa 's' para continuar o 'n' para salir.")
                    if continuar in ["n", "no"]:  
                        print("Gracias por usar el programa!!!")
                        break
                case 3:
                    reprobadas()
                    while True:  
                        continuar = input("\n¡Deseas hacer algo más? (s/n): ").lower().strip()
                        if continuar in ["s", "si", "n", "no"]:
                            break  
                        print("Por favor, ingresa 's' para continuar o 'n' para salir.")
                    if continuar in ["n", "no"]:  
                        print("Gracias por usar el programa!!!")
                        break
                case 4:
                    tP()
                    while True:  
                        continuar = input("\n¡Deseas hacer algo más? (s/n): ").lower().strip()
                        if continuar in ["s", "si", "n", "no"]:
                            break  
                        print("Por favor, ingresa 's' para continuar o 'n' para salir.")
                    if continuar in ["n", "no"]:  
                        print("Gracias por usar el programa!!!")
                        break
                case 5:
                    while True:
                        continuar = input("¿Estás seguro de que quieres salir????? (s/n): ").lower().strip()
                        if continuar in ["s", "si", "n", "no"]:
                            break
                        print("Por favor, ingresa 's' para continuar o 'n' para salir.")
                    if continuar in ["n", "no"]:
                        print("Regresando al menú principal.")
                        break
                    elif continuar in ["s", "si"]:
                        print("Gracias por usar el programa!!")
                        break
                case _:
                    print("Seleccione una opción del 1 al 5 por favor")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__=="__main__":
  menu()