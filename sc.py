# -*- coding: utf-8 -*-
import sys
import argparse

from eratostenes import eratostenes

'''    
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
'''

    
def main():
    '''numArgs = len(sys.argv)
    args = str(sys.argv)
    
    if numArgs < 2:
        print("Ajuda")
        
    elif sys.argv[1] == "erat":
        if numArgs < 3:
            print("Ajuda ERAT")
            return
        try:
            numero = int(sys.argv[2])
            if numero > 2:
                entero = numero
            else:
                print("Tiene que ser mayor que 2")
                return
        except:
            print("Argumento no válido")
            return

        eratostenes(entero, True)
        return
    else:
        print("AJUDA SC")'''

    parser = argparse.ArgumentParser(description='Criba de Eratóstenes')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)

            
if __name__ == "__main__":
    main()
