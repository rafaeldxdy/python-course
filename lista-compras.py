lista_compras = []

while True:

    opcao = input('Digite uma opção para a lista: [i]inserir, [a]pagar, [l]istar ou [s]air: ')

    if opcao == 'i':
        produto = input('Digite o produto que quer adicionar à lista')
        if produto.isdigit() == True:
            print('Por favor, digite uma opção válida.')
            continue
        else:
            lista_compras.append(produto)

    elif opcao == 'a':
        if lista_compras != []:
            for indice in range(0, len(lista_compras)):
                print(f'{indice}: {lista_compras[indice]}')
            indice_produto = int(input('Digite o índice do produto que quer apagar da lista: '))
            lista_compras.pop(indice_produto)
            print(f'A nova lista é: {lista_compras}')
        else:
            print('A lista está vazia!')
            continue
        
    elif opcao == 'l':
        if lista_compras != []:
            for indice in range(0, len(lista_compras)):
                print(f'{indice}: {lista_compras[indice]}')
        else:
            print('A lista está vazia!')

    elif opcao == 's':
        print('Lista de compras finalizada!')
        break
    
    else:
        print('Por favor, digite uma opção válida.')
        continue
