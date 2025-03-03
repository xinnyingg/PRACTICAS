# -*- coding: utf-8 -*-
import os


def carrega(fitxer):
    # Cargamos el fichero y lo pasamos a una lista

    datos=[] #crear variable datos
    with open(fitxer, mode='r') as f:
        #datos = f.readlines()
        #datos = list(f) #lo mismo que readlines
        for linea in f: #hacer la lectura linea en linea
         #   print(linea.rstrip()) #con .rstrip() se consigue eliminar espacio entre lineas
         #   datos.append(linea.rstrip()) #otra manera
            print(tp_ct(linea))

        #print(datos)
    exit()


def tp_ct(t):
    """
    >>> tp_ct('02;00;01;27;82')
    [2, lo que sea del tiempo en centesima de segundo]
    :param t:
    :return:
    """
    # creamos un código de tiemo para calcular tiempos de paso
    # pasamos el tiempo en hh:mm:ss,cc a centésimas de segundo

    ls = t.split(';') #convertir en una lista y .split(;) separar elementos segun lo que este en()
    print(ls)
    return[int(ls[0]), int(ls[1])*60*60*100+int(ls[2])*60*100+int(ls[3])*100+int(ls[4])]

def ct_tp(c):
    # pasamos centésimas de segundo a h,min,seg,cent
    pass


def vuelta_rapida_veh(carr, d):
    # Dada la lista de carrera y un numero de dporsal,
    # determinar en qué vuelta ha realizado el menor tiempo
    pass

def vuelta_rapida_carrera(carr):
    # Determinar cual es la vuelta rapida de toda la carrera
    pass

def imprime_clas(lista):
    # imprime la lista de clasificación
    print('Posicion Equipo Vueltas      Tiempo')
    print('---------------------------------------')
    pass

def classificacio(carr):
    # calcula la clasificacion
    # Crear lista de equipos con un diccionario {dorsal:[vueltas, tiempo],..}
    # añadir una vuelta al dorsal y guardar el último tiempo
    # para la ordenación final
    pass

def primer_paso():
    try:
        with open('codigos.txt', mode='r') as f:
            control = {} #definir un diccionario
            for linea in f:
                coche , cents = tp_ct(linea)
                if coche not in control: #si el coche no este en el diccionario
                    control[coche] = cents #añadir este coche al control
                    if len(control) == 15: #si llega al 15, no hace falta seguir, pq solo hay 15
                        return control
            return control
    except FileNotFoundError as e:
        print("Error:", e)


def main():
    """
    Programa principal  
    llamada a las funciones creadas
    """
    #datos = f.readlines()
    #datos = list(f) #lo mismo que readlines
    print(primer_paso())
    exit()

    #carr = carrega('codigosx.txt')
    ok = False
    #print(carr)
    input()
    os.system('cls')
    while not ok: #obligamos a que el numero entrado sea correcto
        try:
            eq = int(input('entra dorsal (1 a 15):'))
            ok = eq >= 1 and eq <= 15
        except ValueError:
            ok = False
    print('\nVuelta rápida equipo %d ' % eq, end=' --> ')
    vo, te = vuelta_rapida_veh(carr, eq)
    print('vuelta %s en %s' % (vo, ct_tp(te)))
    mvc = vuelta_rapida_carrera(carr)
    print('\nvuelta rápida carrera')
    print('dorsal %2d en la vuelta %2d con un tiempo de %s\n' % (mvc[0], mvc[1], ct_tp(mvc[2])))
    input('seguir...')
    os.system('cls')
    print('Clasificiacion final')
    l = classificacio(carr)
    imprime_clas(l)


if __name__ == "__main__":
    main()
    input('Pulsa Intro... para acabar')
