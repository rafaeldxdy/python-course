# import os - Possibilidade de importar a biblioteca do sistema para realizar a limpeza do Terminal em devidos momentos.

#início do jogo.
iniciar_jogo = 1

while iniciar_jogo == 1:

  # início do jogo pegando do player 01 a palavra secreta e definindo as variáveis de apoio ao jogo.
  palavra_secreta = input('Digite a palavra secreta: ')
  if palavra_secreta.isdigit() == True:
     print('Por favor, digite uma palavra.')
     continue
  nova_palavra_secreta = palavra_secreta.lower()
  aux_palavra = ''
  tentativas = 0

  while True:

    # Pegando a letra secreta do player 02.
    # os.system('clear') - Limpar a tela para que o jogador 2 não veja a palavra secreta.
    letra_secreta = input('Digite uma letra: ')
    tentativas += 1

    nova_letra = letra_secreta.lower()
    
    # Fazendo as devidas tratativas para caso o player 02 digite uma palavra ou um dígito.
    if len(nova_letra) > 1 or nova_letra.isdigit() == True:
        print('Por favor, digite apenas letras.')
        continue

    if nova_letra in nova_palavra_secreta:
      aux_palavra += nova_letra
    
    # Percorrendo a palavra secreta e comparando a letra do usuário se está na palavra secreta, se sim imprime o caractere, senão imprime um asterisco.
    palavra_tentada = ''
    for i in nova_palavra_secreta:
      if i in aux_palavra:
        palavra_tentada += i
      else:
        palavra_tentada += '*'
    print(palavra_tentada)

    # Ao final do jogo, parabenizo o player 02 por ter adivinhado a palavra secreta, revelando-a, mostrando as tentativas feitas e dando a opção de iniciar um novo jogo.
    if nova_palavra_secreta == palavra_tentada:
        # os.system('clear')
        print('Parabéns, você ganhou o jogo!')
        print(f'A palavra secreta era: {nova_palavra_secreta}')
        print(f'Foram feitas {tentativas} tentativas.')
        break
    
  iniciar_jogo = int(input('Você quer parar ou jogar novamente? Digite 0 para parar ou 1 para jogar novamente.'))

print('Fim de jogo.')
