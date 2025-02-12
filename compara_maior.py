primeiro_valor = int(input('Digite o primeiro valor:'))
segundo_valor = int(input('Digite o segundo valor.'))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior que o segundo valor.')
elif (segundo_valor > primeiro_valor):
    print('O segundo valor é maior que o primeiro valor.')
else:
    print('Os valores são iguais.')