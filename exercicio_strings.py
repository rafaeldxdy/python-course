nome = input('Digite seu nome: ')
str_idade = input('Digite sua idade: ')
tamanho_nome = len(nome)
primeira_letra_nome = nome[0]
ultima_letra_nome = nome[(len(nome))-1]
nome_invertido = nome[::-1]

int_idade = int(str_idade)

if nome != '' and  int_idade != '':
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome_invertido}')
    if ' ' in nome:
        print('Seu nome contém espaço!')
    else:
        print('Seu nome não contém espaço!')
    print(f'Seu nome {nome} tem {tamanho_nome} letras.')
    print(f'A primeira letra do seu nome é: {primeira_letra_nome}')
    print(f'A última letra do seu nome é: {ultima_letra_nome}')
else:
    print('Desculpe, você deixou campos vazios!')