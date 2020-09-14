# -*- coding: utf-8 -*-
# Criba de Eratóstenes para práctica de python


def eratostenes(n, verbose=False):
    primo = 2
    indice = 0
    numPrimos = []
    serie = range(primo, n + 1)
    for i in range(n - 1):
        serie[i] = i + 2
        
    while primo * primo < n:
        for i in range(2, n + 1):
            if i * primo <= n:
                serie[(i * primo) - 2] = 0
        for i in range(indice, n):
            if serie[i] <> 0:
                primo = serie[i]
                indice += 1
                break
    contador = 0
    for i in range(n - 1):
        if serie[i] <> 0:
            numPrimos.append(serie[i])
            contador += 1

    print
    print("Criba de Eratóstenes")
    print("====================")
    if verbose:
        print numPrimos
    print("Números primos menores que {}: {}".format(n, contador))
    print("Mayor primo menor que {}: {}".format(n, numPrimos[-1]))
    print
    
    
    

