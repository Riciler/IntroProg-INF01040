# -*- coding: utf-8 -*-

ovo = input()

try:
    quant = float(input())
except:
    print('Quantidade Inválida')
else:
    if quant.is_integer() == False or quant <= 0:
        print('Quantidade Inválida')
    else:
        excs = 0
        if ovo == 'A':
            prec = 12.0
            lim = 50
            if quant > lim:
                quant = lim
                excs = 1
            total = quant * prec
            print(f'Pedido: {quant:.0f} ovos do tipo Simples (A)')
            print(f'Valor Total: R$ {total:.2f}')
            if excs==1:
                print('Limite excedido')
        elif ovo == 'B':
            prec = 15.5
            lim = 30
            if quant > lim:
                quant = lim
                excs = 1
            total = quant * prec
            print(f'Pedido: {quant:.0f} ovos do tipo Recheado (B)')
            print(f'Valor Total: R$ {total:.2f}')
            if excs==1:
                print('Limite excedido')
        elif ovo == 'C':
            prec = 21.3
            lim = 20
            if quant > lim:
                quant = lim
                excs = 1
            total = quant * prec
            print(f'Pedido: {quant:.0f} ovos do tipo Com surpresa (C)')
            print(f'Valor Total: R$ {total:.2f}')
            if excs==1:
                print('Limite excedido')
        else:
            print('Produto inválido')
        


            
            
        
            
        

    