def media(num_1=(int(input("Escribe la primera calificación: "))), 
          num_2=int(input("Escribe la segunda calificación: ")), num_3=int(input("Escribe la tercera calificación: "))):
    resultado= (num_1+num_2+num_3)/3
    return(resultado)
print("El resultado de tus calificaiones es: ", media())