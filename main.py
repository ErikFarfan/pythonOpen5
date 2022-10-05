print('Este programa calcula si un año  bisiesto o no')

anio =int(input('ingrese el año a analizar :  '))

def bisiesto(anio) :

    if anio >= 1582:
        if anio % 4 == 0 and anio % 100 != 0:
            print('este año es bisiesto')
        elif anio % 400 == 0:
            print('Este año es bisiesto')
        else:
            print('Este año no es bisiesto')

    else:
        anio = int(input('ingresa un año mayor a 1582 :  '))
        if anio >= 1582:
            if anio % 4 == 0 and anio % 100 != 0:
                print('este año es bisiesto')
            elif anio % 400 == 0:
                print('Este año es bisiesto')
            else:
                print('Este año no es bisiesto')

bisiesto(anio)














