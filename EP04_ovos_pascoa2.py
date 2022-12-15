# -*- coding: utf-8 -*-

ovo = input()

try:
    quant = int(input())
except ValueError:
    print('Quantidade inválida')
else:
    excs = False
    if ovo == 'A':
        prec = 12.0
        lim = 50
        if quant > lim:
            quant = lim
            excs = True
        total = quant * prec
        print(f'Pedido: {quant} ovos do tipo Simples (A)')
        print('Valor Total: R$','%.2f' % total)
        if excs==True:
            print('Limite excedido')
    elif ovo == 'B':
        prec = 15.5
        lim = 30
        if quant > lim:
            quant = lim
            excs = True
        total = quant * prec
        print(f'Pedido: {quant} ovos do tipo Recheado (B)')
        print('Valor Total: R$','%.2f' % total)
        if excs==True:
            print('Limite excedido')
    elif ovo == 'C':
        prec = 21.3
        lim = 20
        if quant > lim:
            quant = lim
            excs = True
        total = quant * prec
        print(f'Pedido: {quant} ovos do tipo Com surpresa (C)')
        print('Valor Total: R$','%.2f' % total)
        if excs==True:
            print('Limite excedido')
    else:
        print('Produto inválido')
