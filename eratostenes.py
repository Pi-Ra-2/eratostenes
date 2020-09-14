# -*- coding: utf-8 -*-
# Criba de Eratóstenes para práctica de python



def presenta():
    print
    print("Criba de Eratóstenes")
    print("====================")
    print


    
def preguntaNumero():
    while True:
        print
        num = raw_input("Escribe entero mayor que 0: ")
        try:
            numero = int(num)
            if numero > 2:
                return numero
            else:
                print("Tiene que ser mayor que 2")
        except:
            print("Eso no es un número")


def eratostenes(n):
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

    for i in range(n - 1):
        if serie[i] <> 0:
            numPrimos.append(serie[i])
    print numPrimos
    

    
def main():
    salir = False
    p = 2
    while not salir:
        presenta()
        entero = preguntaNumero()
        eratostenes(entero)
        respuesta = raw_input("Deseas salir? (S/N): ")
        if respuesta == "s" or respuesta == "S":
            salir = True
            
if __name__ == "__main__":
    main()
