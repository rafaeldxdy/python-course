# Validação de CPF usando o algoritmo oficial da Receita Federal
# CPF Validation using the official Brazilian algorithm

# Verifica se o CPF informado tem 11 dígitos numéricos
def fn_cpf_candidate(cpf):
    if len(cpf) != 11 or not cpf.isnumeric():
        return False
    else:
        return True

# Calcula o primeiro dígito verificador do CPF
# Calculates the first check digit of the CPF
def check_first_digit(cpf):
    result = 0
    counter = 10

    for i in range(len(cpf) - 2):
        result += int(cpf[i]) * counter
        counter -= 1

    result *= 10
    result %= 11

    if result > 9:
        result = 0

    return result

# Calcula o segundo dígito verificador do CPF
# Calculates the second check digit of the CPF
def check_second_digit(cpf):
    result = 0
    counter = 11

    for i in range(len(cpf) - 1):
        result += int(cpf[i]) * counter
        counter -= 1

    result *= 10
    result %= 11

    if result > 9:
        result = 0

    return result

# Compara os dígitos informados com os dígitos calculados
# Compares the input digits with the calculated digits
def validate_cpf(cpf, first_digit, second_digit):
    if int(cpf[9]) == first_digit and int(cpf[10]) == second_digit:
        return True
    else:
        return False

start_program = True
continue_verify = True

# Loop principal do programa
# Main program loop
while start_program:

    cpf = input('Type your CPF (just numbers): ')
    valid_candidate_cpf = fn_cpf_candidate(cpf)

    # Verifica se o CPF tem formato válido (11 dígitos numéricos)
    if not valid_candidate_cpf:
        print('Please, type a valid CPF.')
        continue
    else:
        # Calcula os dígitos verificadores
        # Calculates the check digits
        first_digit_cpf = check_first_digit(cpf)
        second_digit_cpf = check_second_digit(cpf)

        # Verifica se o CPF é válido
        # Validates the CPF
        is_valid = validate_cpf(cpf, first_digit_cpf, second_digit_cpf)

        if is_valid:
            print(f'The {cpf} is a valid CPF!')
        else:
            print(f'The {cpf} is not a valid CPF! Try again.')

    # Pergunta se o usuário deseja validar outro CPF
    # Asks the user whether to validate another CPF
    while continue_verify:

        continue_verify = input('Do you want to try a new CPF? [Y]es or [N]o: ')

        try:
            if continue_verify[0] in ['Y', 'y']:
                break
            elif continue_verify[0] in ['N', 'n']:
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
