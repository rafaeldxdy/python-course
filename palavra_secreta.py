import os

sair = False

while not sair:
  
    tentativas = 0
    palavra_secreta = input('Digite a palavra secreta: ')
    os.system('clear')
    if palavra_secreta.isdigit() or any(char in "!@#$%^&*()-+?_=,<>/;" for char in palavra_secreta):
        print('Digite uma palavra válida.')
        continue
    palavra_secreta = palavra_secreta.lower()

    mostra_letra = ['*'] * len(palavra_secreta)
    print(''.join(mostra_letra))
    
    while '*' in mostra_letra:
        letra = input('Digite uma letra: ')
        if letra.isdigit() or letra in '!@#$%^&*()-+?_=,<>/;' or len(letra) > 1:
            print('Digite uma letra válida.')
            continue
        letra = letra.lower()
            
        tentativas += 1

        for index, char in enumerate(palavra_secreta):
            if letra == char:
                mostra_letra[index] = letra

        print(f'A palavra secreta é: {"".join(mostra_letra)}')

    os.system('clear')
    continuar = input(f'Parabens, voce adivinhou a palavra secreta em {tentativas} tentativas. Gostaria de jogar novamente? [S]im ou [N]ão: ')
    if continuar.lower().startswith('n'):
        sair = True
