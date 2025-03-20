'''
Autor: Tomàs Lloret Martínez
Fecha: 13/03/2025
APA - Práctica 2: Manejo de números primos

Módulo que define funciones con números primos.

>>> esPrimo(4)
False

>>> esPrimo(-2)
True

>>> esPrimo(1023)
False

>>> esPrimo(1021)
True

'''

'''
Determinación de la primalidad y decomposición de un número en factores primos
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()



def esPrimo(numero):
    '''
    Devuelve true si es primo y false si no lo es
    '''
    for test in range(2, numero):
        if numero % test == 0:
            return False
    return True

def primos(numero):
    '''
    Devuelve tupla con los primos menores a numero
    '''
    primos = []
    for n in range(2, numero):
        if esPrimo(n):
            primos.append(n)
    return tuple(primos)

def descompon(numero):
    '''
    Deveuelve tupla con la decomposición en primos de numero
    '''
    factores = []
    for primo in primos(numero + 1):  # usamos funcion anterior
        while numero % primo == 0:   # divisible por el primo
            factores.append(primo)
            numero //= primo
        if numero == 1:              # acabamos en llegar a 1
            break
    return tuple(factores)    

'''
Obtención del mínimo común múltiplo y el máximo común divisor
'''

def mcm(numero1, numero2):
    '''
    Devuelve el mínimo común múltiplo de los dos numeros
    '''
    desc1 = descompon(numero1) # Descomponemos los dos numeros
    desc2 = descompon(numero2)

    factores_mcm = list(desc1) # creamos una lista que usaremos para almacenar los factores que dan el mcm

    # añadimos los de la segunda lista quitando los que haya ya
    for f in desc2:
        if factores_mcm.count(f) < desc2.count(f): #si hay mas x en desc2 que en factores_mcm, agrega una x
            factores_mcm.append(f)

    # multiplicamos la lista
    mcm = 1
    for i in factores_mcm:
        mcm = mcm * i

    return mcm
    
def mcd(numero1, numero2):
    '''
    devuelve el màximo común divisor de los dos numeros
    '''
    desc1 = descompon(numero1) # Descomponemos los dos numeros
    desc2 = descompon(numero2)

    factores_mcd = list(desc1) # creamos una lista que usaremos para almacenar los factores que dan el mcd

    # añadimos los de la segunda lista quitando los que haya ya
    for f in desc2:
        if factores_mcd.count(f) > desc2.count(f): #si hay mas x en factores estas no son necesarias
            factores_mcd.remove(f)

    # ahora tenemos una lista que contiene tambien los numeros que tiene desc1 que no tiene desc2, los quitamos
    for f in factores_mcd:
        if factores_mcd.count(f) > desc2.count(f): #si hay mas x en factores estas no son necesarias
            factores_mcd.remove(f)

    # multiplicamos la lista
    mcd = 1
    for i in factores_mcd:
        mcd = mcd * i

    return mcd

'''
Obtención del mínimo común múltiplo y el máximo común dicisor para un número arbitrario de argumentos
'''
