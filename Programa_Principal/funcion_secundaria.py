def main():
    
    horas = int(input('Ingrese el número de horas totales en el parcial de la materia que desea consultar: '))
    faltas = int(input('Ingrese el número de faltas: '))

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


if __name__=="__main__":
    main()
