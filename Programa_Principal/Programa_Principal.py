from menus import media
from Funcion_externa import main 
def asistencias():
   semestre= int(input("En que semestre estas actualmente:"))
   na= int(input("Cuantas materias no acreditadas tienes?: "))
  
  
  


def menu():
  while True:
    print("Bienvenido al programa donde vas a poder consultar distintas cosas acerca de tu semestre de la universidad en la UACH\n" ) 
    print("A continuación se muestran las opciones a las que puede acceder: ")
    print("Opcion 1: Promedio de tus calificaciones de todo el semestre:")
    print("Opicón 2: Tus asistencias a clases durante el semestre")
    print("Opción 3: Riesgo que tienes de ser dado de bajo por tus No Acreditadas")
    print("Opción 4: Cuanto te falta para aprobar el semestre, considerando la calificación mínima como 7")
    print("Opción 5: Salir")
    opcion= int(input("Digita la opción que deseas seleccionar hoy: "))
    match(opcion):
      case(1):
        media()
        while True:  #
            continuar = input("\n¡Deseas hacer algo más? (s/n): ").lower().strip()
            if continuar in ["s", "si", "n", "no"]:
               break  
            print("Por favor, ingresa 's' para continuar o 'n' para salir.")
        if continuar in ["n", "no"]:  
            print("Gracias por usar el programa!!!")
            break
      case(2):
        main()
        continuar= input("\n¿Deseas hacer algo más? (s/n): ").lower()
        if continuar != "s":
          print("Gracias por usar el programa!!")
          break
      case(3):
          
         
           



        


if __name__=="__main__":
  menu()