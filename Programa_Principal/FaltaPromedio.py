#Saber cuanto me falta en el tercer parcial para poder aprobar el semestre
def tP():
    ciclo=True
    P1=0
    P2=0
    calif=0
    califFinal=0
    while ciclo==True:
        
        try:
            P1=float(input("Ingresa tu primer calificación en base a 10: "))
            P2=float(input("Ingresa tu segunda calificación en base a 10: "))   
            calif=(P1*.3)+(P2*.3)
            califFinal=float(7-calif)
            califParcial=float(califFinal/.4) 
            if  5<=califParcial<=10:
                print("Tu calificación necesaria para aprobar es ",califParcial)
                ciclo=False
            elif 0<=califParcial<=5:
                print("Tranquilo, puedes relajarte un poco \U0001F60E necesitas un", califParcial)
            else:
                print("Ve ahorrando para el extra \U0001F62D \U0001F62D \U0001F62D	")
                ciclo=False
        except ValueError:
            print(" Digita un valor númerico")
            ciclo=False
    
    #Calif es la calificacion de los dos parciales
    #Calif final es la calificacion final necesaria
    #Calif Parcial es la calificacion del puro examen parcial sin sacar el porcentaje
    
if __name__=="__main__":
    tP()