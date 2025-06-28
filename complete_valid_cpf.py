# Validate CPF

#CPF Algorithm

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

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
   *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
      77 40 54 64 14 24 40 36  0 14

      Somar todos os resultados:
      77+40+54+64+14+24+40+36+0+14 = 363
      Multiplicar o resultado anterior por 10
      363 * 10 = 3630
      Obter o resto da divisão da conta anterior por 11
      3630 % 11 = 0
      Se o resultado anterior for maior que 9:
          resultado é 0
          contrário disso:
              resultado é o valor da conta

              O segundo dígito do CPF é 0
              """


# Verify if a CPF candidate can be calid
def fn_cpf_candidate(cpf):

    # valid_candidate_cpf
    if len(cpf) != 11 or cpf.isnumeric() != True:
        return False
    else:
        return True

# Validate the first digit 
def check_first_digit(cpf):

    result = 0
    counter = 10

    for numbers in range(len(cpf) - 2):
        result = result + (int(cpf[numbers]))*counter
        counter -= 1
    result *= 10
    result %= 11

    if result > 9:
        result = 0
    
    return result

# Validate the second digit 
def check_second_digit(cpf):

    result = 0
    counter = 11

    for numbers in range(len(cpf) - 1):
        result = result + (int(cpf[numbers]))*counter
        counter -= 1
    result *= 10
    result %= 11

    if result > 9:
        result = 0
    
    return result

# Validate CPF
def validate_cpf(cpf, first_digit, second_digit):

    if int(cpf[9]) == first_digit and int(cpf[10]) == second_digit:
        return True
    else:
        return False
    
start_program = True
continue_verify = True

while start_program:

    cpf = input('Type your CPF (just numbers): ')
    valid_candidate_cpf = fn_cpf_candidate(cpf)

    if valid_candidate_cpf == False:
        print('Please, type a valid CPF.')
        continue

    else:

        first_digit_cpf = check_first_digit(cpf)
        second_digit_cpf = check_second_digit(cpf)
        cpf_candidate = validate_cpf(cpf, first_digit_cpf, second_digit_cpf)

        if cpf_candidate == True:
            print(f'The {cpf} is a valid CPF!')
        else:
            print(f'The {cpf} is not a valid CPF! Try again.')

    while continue_verify:

        continue_verify = input('Do you want to try a new CPF? [Y]es or [N]o: ')

        try:
            if continue_verify[0] == 'Y' or continue_verify[0] == 'y':
                break
            elif continue_verify[0] == 'N' or continue_verify[0] == 'n':
                start_program = False
                print('Bye, bye.')
                break
            else:
                print('Please, type a valid option!')
                continue

        except IndexError:
            continue_verify = True
            print('Please, type a valid option!')
            continue
