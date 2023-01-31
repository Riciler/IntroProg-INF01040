# -*- coding: utf-8 -*-
"""

"""

voto = 0
urna = []
ocorr = []

while True:
    voto = int(input())
    if voto < 1 or voto > 24:
        pass
    else:
        if voto not in urna:
            ocorr.append(voto)
        urna.append(voto)
    if voto == 0:
        break
    
ocorr.sort(); urna.sort()
cont = []
for e in ocorr:
    cont.append(urna.count(e))

tot = len(urna)
print(f"TOTAL DE VOTOS = {tot}")

i=0
for e in ocorr:
    print(f'JOGADOR = {e}, VOTOS = {cont[i]}, PERCENTUAL = {int((100*cont[i])/tot)}%')
    i = i + 1
    
indmaior = cont.index(max(cont))
print(f'MELHOR JOGADOR = {ocorr[indmaior]}')