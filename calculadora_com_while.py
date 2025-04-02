controle = 1

while controle != 0:
    try:
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))
        operador = input('Digite um operador, sendo: +,-,/,*: ')

        if operador == '+':
            resultado = primeiro_numero + segundo_numero
            print(f'O resultado é: {resultado}')
            controle = int(input('Digite 1 para continuar ou 0 para sair.'))
        elif operador == '-':
            resultado = primeiro_numero - segundo_numero
            print(f'O resultado é: {resultado}')
            controle = int(input('Digite 1 para continuar ou 0 para sair.'))
        elif operador == '*':
            resultado = primeiro_numero * segundo_numero
            print(f'O resultado é: {resultado}')
            controle = int(input('Digite 1 para continuar ou 0 para sair.'))
        elif operador == '/':
            resultado = primeiro_numero / segundo_numero
            print(f'O resultado é: {resultado}')
            controle = int(input('Digite 1 para continuar ou 0 para sair.'))
        else:
            print('Digite um valor e um operador válido.')
    except:
        print('Digite um número e um operador válido.')
