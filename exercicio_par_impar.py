str_numero = input('Digite um número: ')

try:
    int_numero = int(str_numero)

    if int_numero % 2 == 0:
        print('Este número é par!')
    else:
        print('Este número é ímpar!')
except:
    print('Você não digitou um número inteiro.')