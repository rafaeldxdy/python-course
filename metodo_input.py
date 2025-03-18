numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

int_numero1 = int(numero1)
int_numero2 = int(numero2)

if int_numero1 > int_numero2:
    print(f'O número {int_numero1} é maior que o número {int_numero2}')
elif int_numero2 > int_numero1:
    print(f'O número {int_numero2} é maior que o número {int_numero1}')
else:
    print('Os números são iguais')
