import os

lista_compras = []

while True:

    opcao = input('''Selecione a opção desejada: \n [l]istar \n [i]nserir \n [r]emover \n [s]air \n''')

    if opcao.isalpha() == False or len(opcao) > 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Por favor, selecione uma opção válida.')
        continue

    if opcao.lower() == 'l':
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(lista_compras) == 0:
            print('Sua lista está vazia.')
        else:
            for indice, item in enumerate(lista_compras):
                print(f'{indice}. {item}')

    elif opcao.lower() == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        item_lista = input('O que gostaria de inserir? ')
        if item_lista in lista_compras:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Esse item já está na lista.')
            continue
        else:
            lista_compras.append(item_lista)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Item inserido com sucesso! Sua nova lista é:')
            for indice, item in enumerate(lista_compras):
                print(f'{indice}. {item}')

    elif opcao.lower() == 'r':

        if len(lista_compras) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Sua lista está vazia.')
            continue

        os.system('cls' if os.name == 'nt' else 'clear')

        for indice, item in enumerate(lista_compras):
            print(f'{indice}. {item}')
        indice_lista = input('Qual item gostaria de remover? ')

        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            int_indice_lista = int(indice_lista)

            if int_indice_lista < 0 or int_indice_lista >= len(lista_compras):
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Por favor, selecione um índice válido.')
                continue

            del lista_compras[int_indice_lista]
            print('Item removido com sucesso! Sua nova lista é:')
            for indice, item in enumerate(lista_compras):
                print(f'{indice}. {item}')
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Por favor, selecione um índice válido.')
            continue

    elif opcao.lower() == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    else:
        print('Por favor, selecione una opção válida.')
print('Saindo do programa...')
