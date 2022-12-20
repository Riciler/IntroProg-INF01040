# -*- coding: utf-8 -*-
"""
 Se o termo anterior for par, o próximo termo da sequência será a metade do anterior (N/2). 
 Caso o termo anterior seja ímpar, o próximo será 3 vezes o termo anterior mais 1 (3N+1)
 
 
Conjectura de Collatz para N = 12
6    ######
3    ###
10   ##########
5    #####
16   ################
8    ########
4    ####
2    ##
1    #
 
 
Conjectura de Collatz para N = 3
10   ##########
5    #####
16   ################
8    ########
4    ####
2    ##
1    #

"""

try:
    N = int(input())
except ValueError:
    print('Entrada inválida')
else:  
    if N <= 0:
        print('Entrada inválida')
    else:
        print(f'Conjectura de Collatz para N = {N}')
        while True:
            if N%2==0:
                N = N//2
            elif N%2==1:
                N = (3*N)+1
            bar = int(N) * '#'
            print(f'{N}\t',bar)
            if N == 1:
                break