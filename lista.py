indice = 0

# Criando uma lista
lista_frutas = ['maçã', 'banana', 'pêra', 'morango']

# Imprimindo a lista
print(f'Sua lista é: {lista_frutas}')

for frutas in lista_frutas:
    # Percorrendo uma lista por seus índices
    print(f'Índice: {indice}. Valor: {lista_frutas[indice]}')
    indice += 1

# Trocando o terceiro item da lista
lista_frutas[2] = 'tomate'
print(lista_frutas)

# Removendo o último item da lista
lista_frutas.pop()
print(lista_frutas)

# Acrescenta um item ao fim da lista
lista_frutas.append('uva')
print(lista_frutas)

# Insere um item numa posição específica da lista
lista_frutas.insert(1, 'Caqui')

# Removendo um item numa posição específica da lista
del lista_frutas[3]s

# Limpando a lista
lista_frutas.clear()

frutas_frescas = ['banana', 'maçã', 'morango']
print(frutas_frescas)
frutas_secas = ['ameixa', 'passas']
print(frutas_secas)
todas_frutas = frutas_frescas + frutas_secas
print(todas_frutas)

mais_frutas = []
mais_frutas.extend(todas_frutas)
print(mais_frutas)

# Para copiarmos uma lista em outra, usamos:
nova_lista = mais_frutas.copy()
print(nova_lista)
