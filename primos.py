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

def esPrimo(numero):
    '''
    Devuelve true si es primo y false si no lo es

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    '''
    for test in range(2, numero):
        if numero % test == 0:
            return False
    return True

def primos(numero):
    '''
    Devuelve tupla con los primos menores a numero

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    '''
    primos = []
    for n in range(2, numero):
        if esPrimo(n):
            primos.append(n)
    return tuple(primos)

def descompon(numero):
    '''
    Deveuelve tupla con la decomposición en primos de numero

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    '''
    factores = []
    div = 2
    while div * div <= numero:
        while numero % div == 0:   # divisible por el primo
            factores.append(div)
            numero //= div
        div += 1
    if numero > 1:               # si queda un número primo
        factores.append(numero)
    return tuple(factores)   

'''
Obtención del mínimo común múltiplo y el máximo común divisor
'''

def mcm(numero1, numero2):
    '''
    Devuelve el mínimo común múltiplo de los dos numeros
    
    >>> mcm(90, 14)
    630
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

    >>> mcd(924, 780)
    12
    '''
    desc1 = list(descompon(numero1)) # Descomponemos los dos numeros
    desc2 = list(descompon(numero2))

    mcd = 1

    for i in desc1: # recorremos la primera lista
        if i in desc2:
            desc2.remove(i)
            mcd = mcd * i

    return mcd

'''
Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos
'''

def mcmN(*numeros):
    '''
    MCM de varis numeros
    
    >>> mcmN(42, 60, 70, 63)
    1260
    '''
    if not numeros:
        return 1
    result = numeros[0]
    for numero in numeros[1:]:
        result = mcm(result, numero)
    return result 

def mcdN(*numeros):
    '''
    MCD de varis numeros
    
    >>> mcdN(840, 630, 1050, 1470)
    210
    '''
    if not numeros:
        return 1
    result = numeros[0]
    for numero in numeros[1:]:
        result = mcd(result, numero)
    return result 

if __name__ == '__main__':
    import doctest
    doctest.testmod()

