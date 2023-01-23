# -*- coding: utf-8 -*-
"""
a soma dos números inteiros no intervalo [2, 5] é 14 = (2+3+4+5). O programa também deve mostrar o número que divide o intervalo ao meio,
caso o tamanho dele seja ímpar, ou os dois números, caso o tamanho do intervalo seja par. Por exemplo, os números que dividem o intervalo [2, 5] são:
3 e 4. O usuário pode informar o intervalo em ordem crescente ou decrescente, ou seja, [2,5] e [5,2]
são ambas entradas válidas para a mesma soma.


2  6
Início do intervalo: 2
Fim do intervalo: 6
Somatório do intervalo 20
Metade do intervalo 4
"""
# entrada de dados

inicio = int(input())
final = int(input())
intervalo = final - inicio

# gerando a lista

termo = inicio
lista = []

if intervalo >= 0:
    while True:
        lista.append(termo)
        termo = termo + 1
        if termo == final + 1:
            break
else:
    while True:
        lista.append(termo)
        termo = termo - 1
        if termo == final - 1:
            break
    
# realizando a soma

soma = 0
for e in lista:
    soma = soma + e
    
# encontrando a metade do conjunto

if len(lista) % 2 == 1:
    ind = int(len(lista)/2-0.5)
    metade = lista[ind]
    
else:
    ind = int(len(lista)/2-0.5)
    metade1 = lista[ind]
    metade2 = lista[ind+1]
    metades = [metade1, metade2]
    metades.sort()
    
# saída de dados

print(f'Início do intervalo: {inicio}')
print(f'Fim do intervalo: {final}')
print(f'Somatório do intervalo {soma}')
if len(lista) % 2 == 1:
    print(f'Metade do intervalo {metade}')
else:
    print(f'Metade do intervalo {metades[0]} e {metades[1]}')





