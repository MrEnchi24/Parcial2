def main():

    ciclo = True
    while ciclo == True:

        horas = input('Ingrese el número de horas totales en el semestre de la materia que desea consultar: ')
        faltas = input('Ingrese el número de faltas: ')
        
        if not horas.isdigit() or not faltas.isdigit(): 
            print("\nIngrese datos válidos. \nLas horas y faltas deben ser números enteros positivos\n")
        else:
            horas=int(horas)
            faltas=int(faltas)

            if faltas>horas:
                print('\nLas faltas deben ser iguales o menores a las horas de la materias\n')
            else:
                asistencia = horas - faltas
                asistencia = asistencia / horas
                porcentaje = asistencia * 100
                porcentaje = str(porcentaje)+'%'

                print('\nEl porcentaje de asistencia es de: ', porcentaje)

                if asistencia >= 0.80:
                    print('Aún puedes presentar el \033[1mExamen Ordinario\033[0m \U0001F600')
                elif asistencia < 0.80 and asistencia >= 0.60:
                    print('Ya no puedes hacer el \033[1mOrdinario\033[0m \U0001F61F, tienes que  hacer el \033[1mExtra\033[0m \U0001F923')
                elif asistencia < 0.60:
                    print('Ya no puedes hacer el ni el \033[1mOrdinario\033[0m ni el \033[1mExtra\033[0m \U0001F63F')
                ciclo = False



if __name__=="__main__":
    main()
