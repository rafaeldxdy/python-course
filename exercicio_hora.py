str_hora = input('Que horas são? ')

try:
    int_hora = int(str_hora[0:2])
    
    if int_hora >= 0 and int_hora <= 11:
        print('Bom dia!')
    elif int_hora >= 12 and int_hora <= 17:
        print('Boa tarde!')
    elif int_hora >= 18 and int_hora <= 23:
        print('Boa noite!')
    else:
        print('Por favor, digite um valor de hora válido.')
except:
    print('Por favor, digite um valor de hora válido.')
