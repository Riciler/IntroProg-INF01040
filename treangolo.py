
print('Insira o lado 1: \n>>>')
lado1 = float(input())

print('Insira o lado 2: \n>>>')
lado2 = float(input())

print('Insira o lado 3: \n>>>')
lado3 = float(input())

if lado1 > lado2+lado3 or lado2 > lado1+lado3 or lado3 > lado2+lado1:  #sepa seja >=
    print('triângulo inválido')
elif lado1 == 0 or lado2 == 0 or lado3 == 0:
    print('triângulo inválido')
elif lado1 == lado2 == lado3:
    print('triângulo equilátero')
elif lado1 != lado2 != lado3:
    print('triângulo escaleno')
else:
    print('triângulo isósceles')
    

