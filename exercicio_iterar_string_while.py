nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
novo_nome = ''
contador = 0

while contador < tamanho_nome:
    if contador % 2 == 0:
        novo_nome += nome[contador].upper()
    else:
        novo_nome += nome[contador].lower()
    contador += 1

print(f'Seu nome formatado é: {novo_nome}')