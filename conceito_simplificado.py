# -*- coding: utf-8 -*-
"""
lê um valor para a nota e outro para frequência
dando o conceito do aluno como saída
"""

# Entrada de dados
print('Digite um valor para a nota')
nota = float(input())

print('Digite um valor para a frequência')
freq = float(input())

# Controle de entrada
if nota>100 or nota<0 or freq>100 or freq<0:
    print('Entrada inválida')
else:
    if nota>=60 and freq>=75:
        print('Aprovado')
    elif nota<60 and freq>=75:
        print('Exame')
    else:
        print('Reprovado') 


