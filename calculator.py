sair = ''

while sair != 's':

    str_primeiro_numero = input('Digite o primeiro número ou "s" para sair: ')
    if str_primeiro_numero.lower().startswith('s') == True:
        break

    try:

        primeiro_numero = float(str_primeiro_numero)
        segundo_numero = float(input('Digite o segundo número: '))
    
    except:
        print('Por favor, digite um número válido.')
        continue

    operador = input('Digite um operador entre: +, -, *, / : ')

    while operador not in '+-*/' or len(operador) > 1:
        operador = input('Digite um operador válido, entre: +, -, *, / : ')
    
    if operador == '+':
        print(f'O resultado de {primeiro_numero} + {segundo_numero} = ', primeiro_numero + segundo_numero)
    elif operador == '-':
        print(f'O resultado de {primeiro_numero} - {segundo_numero} = ', primeiro_numero - segundo_numero)
    elif operador == '*':
        print(f'O resultado de {primeiro_numero} * {segundo_numero} = ', primeiro_numero * segundo_numero)
    elif operador == '/':
        print(f'O resultado de {primeiro_numero} / {segundo_numero} = ', primeiro_numero / segundo_numero)
    else:
        print('Nunca deve chegar aqui')
    
    sair = input('Digite "s" para sair ou outra tecla para continuar. ').lower()
    if sair.startswith('s') == True:
        break
    else:
        continue
