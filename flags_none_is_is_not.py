numero = None
numero = input('Digite um número: ')
numero_int = int(numero)

if numero_int is not None:
    if numero_int > 10:
        print('Este número é maior que 10!')
    elif numero_int < 10:
        print('Este número é menor que 10!')
    else:
        print('Este número é 10!')
else:
    print('Valor inválido.')