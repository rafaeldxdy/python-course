import os

lista_compras = []

while True:

    # Limpa a tela no início de cada iteração do loop principal
    os.system('cls' if os.name == 'nt' else 'clear')

    opcao = input('''Selecione a opção desejada: \n [l]istar \n [i]nserir \n [r]emover \n [s]air \n''')

    if opcao.isalpha() == False or len(opcao) > 1:
        print('Por favor, selecione uma opção válida.')
        continue

    if opcao.lower() == 'l':
        if len(lista_compras) == 0:
            print('Sua lista está vazia.')
        else:
            for indice, item in enumerate(lista_compras):
                print(f'{indice}. {item}')

    elif opcao.lower() == 'i':
        item_lista = input('O que gostaria de inserir? ')
        if item_lista in lista_compras:
            print('Esse item já está na lista.')
            continue
        else:
            lista_compras.append(item_lista)
            print(f'"{item_lista}" inserido com sucesso!')
            for indice, item in enumerate(lista_compras):
                print(f'{indice}. {item}')

    elif opcao.lower() == 'r':

        if len(lista_compras) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Sua lista está vazia. Nada para remover.')
            continue

        for indice, item in enumerate(lista_compras):
            print(f'{indice}. {item}')
        indice_lista = input('Qual item gostaria de remover? ')

        try:
            int_indice_lista = int(indice_lista)

            if int_indice_lista < 0 or int_indice_lista >= len(lista_compras):
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Por favor, selecione um índice válido.')
                continue

            del lista_compras[int_indice_lista]
            print('Item removido com sucesso!')
            for indice, item in enumerate(lista_compras):
                print(f'{indice}. {item}')
        except:
            print('Por favor, selecione um índice válido.')
            continue

    elif opcao.lower() == 's':
        break

    else:
        # Este else é alcançado se a opção for uma letra única, mas não l, i, r ou s
        print('Por favor, selecione uma opção válida.')

    input('\nPressione Enter para continuar...') # Pausa para o usuário ver a saída
print('Saindo do programa...')
