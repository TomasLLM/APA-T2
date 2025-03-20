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
import math

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

    # He encontrado la funcion math.prod() que multiplica elementos de una lista

    
