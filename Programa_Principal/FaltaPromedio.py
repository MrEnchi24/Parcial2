#Saber cuanto me falta en el tercer parcial para poder aprobar el semestre
def tP():
    P1=0
    P2=0
    calif=0
    califFinal=0
    P1=float(input("Ingresa tu primer calificación en base a 10: "))
    
    P2=float(input("Ingresa tu segunda calificación en base a 10: "))
    calif=(P1*.3)+(P2*.3)
    califFinal=float(7-calif)
    califParcial=float(califFinal/.4)
    if  0<=califParcial<=10:
        print("Tu calificación necesaria para aprobar es ",califParcial)
    else:
        print("Ve ahorrando para el extra")
    
    #Calif es la calificacion de los dos parciales
    #Calif final es la calificacion final necesaria
    #Calif Parcial es la calificacion del puro examen parcial sin sacar el porcentaje
    
if __name__=="__main__":
    tP()