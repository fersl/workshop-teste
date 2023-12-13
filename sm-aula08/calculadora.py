operacao = int(input('Qual operação quer fazer? \n 1) soma\n 2) subtração\n 3) multiplicação\n 4) Divisão\n'))
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))

if operacao == 1:
    print(num1 + num2)

if operacao == 2:
    print(num1 - num2)

if operacao == 3:
    print(num1 * num2)

if operacao == 4:
    print(num1 / num2)

