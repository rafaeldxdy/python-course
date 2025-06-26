# A basic program that validates the first digit of a CPF number.
# CPF is a Brazilian individual taxpayer registry identification.

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890) 
   10  9  8  7  6  5  4  3  2
   *  7   4  6  8  2  4  8  9  0
      70  36 48 56 12 20 32 27 0

      Somar todos os resultados: 
      70+36+48+56+12+20+32+27+0 = 301
      Multiplicar o resultado anterior por 10
      301 * 10 = 3010
      Obter o resto da divisão da conta anterior por 11
      3010 % 11 = 7
      Se o resultado anterior for maior que 9:
          resultado é 0
          contrário disso:
              resultado é o valor da conta

              O primeiro dígito do CPF é 7
              """

sum_digits = 0
counter = 10

while True:
    
    cpf = input('Type your CPF: ')

    new_cpf = cpf.replace('.', '').replace('-', '')

    if len(new_cpf) != 11 or not new_cpf.isdigit():
        print("Invalid CPF format. Please enter a valid CPF with 11 digits.")
        continue

    for i in range(len(new_cpf) - 2):

        if new_cpf[i].isdigit() == True:
            sum_digits = sum_digits + (int(new_cpf[i]) * counter)
            counter = counter - 1

    result = sum_digits * 10 % 11

    result = 0 if result > 9 else result

    print(f"The first digit of the CPF is {result} and it's a valid digit.")
    break
