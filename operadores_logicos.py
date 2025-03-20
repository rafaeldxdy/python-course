senha_permitida = '123456'

entrada = input('[E]ntrar [S]air ')

if entrada != 'E':
    print('Você saiu!')
else:
    senha_digitada = input('Digite sua senha: ')
    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrada autorizada!')
    else:
        print('Entrada negada!')