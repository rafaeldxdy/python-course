condicao = True

while condicao:
    nome = input('Digite seu nome ou "Sair" para finalizar: ')
    if nome == 'Sair':
        break
    else:
        print(f'Seu nome é: {nome}')