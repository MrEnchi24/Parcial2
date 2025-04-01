def media(): 
    while True:
        try:
            calificacion_1 = float(input("Ingresa tu calificación del primer parcial: "))
            if 0 <= calificacion_1 <= 10:
                break  
            else:
                print("La calificación debe estar entre 0 y 10")
        except ValueError:
            print("Favor de ingresar un número")
    
    while True:
        try:
            calificacion_2 = float(input("Ingresa tu calificación del segundo parcial: "))
            if 0 <= calificacion_2 <= 10:
                break  
            else:
                print("La calificación debe estar entre 0 y 10")
        except ValueError:
            print("Favor de ingresar un número")
    
    while True:
        try:
            calificacion_3 = float(input("Ingresa tu calificación del tercer parcial: "))
            if 0 <= calificacion_3 <= 10:
                break  
            else:
                print("La calificación debe estar entre 0 y 10")
        except ValueError:
            print("Favor de ingresar un número")
    
    promedio = (calificacion_1 * .30) + (calificacion_2 * .30) + (calificacion_3 * .40)
    print("Tu promedio es de: ", promedio)
    if promedio==10:
        print("WOOOOOOOOW sacaste calificación perfecta \U0001F44C \U0001F973")
    elif 9 <= promedio <10:
        print("Felicidades sacaste muy buena calificación \U0001F606")
    elif 8 <= promedio <8.999:
        print("Muy bien sigue siendo una buena calificación \U0001F60E ")
    elif 7.2 <= promedio <7.999:
        print("Uffff se pasó con eso nos vamos felices \U0001F979 ")
    elif 7<= promedio<=7.1:
        print("AYYYYY apenitas pero se pudooooooooo!! \U0001F47B ")
    elif 6.7<= promedio<=6.9:
        print("Digale a su profe que no sea gacho y lo paseeee \U0001F62D")
    else:
        print("Ni modo no pasa nada, a echarle ganas al extra o a recursar la materia \U0001F642 ")
    
    return promedio