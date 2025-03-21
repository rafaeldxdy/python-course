nome = input('Digite seu nome: ')
str_idade = input('Digite sua idade: ')

int_idade = int(str_idade)

if nome != '' and  int_idade != '':
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[-len(nome),0]}')
    if ' ' in nome:
        print('Seu nome contém espaço!')
    else:
        print('Seu nome não contém espaço!')
    print(f'Seu nome {nome} tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é {nome[len()-1]}')
else:
    print('Desculpe, você deixou campos vazios!')