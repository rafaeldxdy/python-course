# in / not in

palavra = input('Digite uma palavra: ')
encontrar = input('Digite o que quer encontrar na palavra: ')

if encontrar in palavra:
    print(f'{encontrar} está em {palavra}')
elif encontrar not in palavra:
    print(f'{encontrar} não está em {palavra}')
else:
    print('Erro!')