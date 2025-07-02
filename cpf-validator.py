# CPF Validator in Python 🇧🇷
# Author: Rafael Ribeiro
# Improved with the help of AI (ChatGPT) 🤖
# Description: Validates Brazilian CPF numbers using the official algorithm,
# written for learning purposes and personal development.

# Validação de CPF usando o algoritmo oficial da Receita Federal
# CPF validation using the official Brazilian algorithm


# Verifica se o CPF informado tem 11 dígitos numéricos
# Checks if the input CPF has 11 numeric digits
def is_valid_cpf_format(cpf):
    return len(cpf) == 11 and cpf.isdigit()


# Calcula o primeiro dígito verificador do CPF
# Calculates the first check digit of the CPF
def calculate_first_digit(cpf):
    total = 0
    weight = 10

    for i in range(9):
        total += int(cpf[i]) * weight
        weight -= 1

    digit = (total * 10) % 11
    return 0 if digit > 9 else digit


# Calcula o segundo dígito verificador do CPF
# Calculates the second check digit of the CPF
def calculate_second_digit(cpf):
    total = 0
    weight = 11

    for i in range(10):
        total += int(cpf[i]) * weight
        weight -= 1

    digit = (total * 10) % 11
    return 0 if digit > 9 else digit


# Compara os dígitos informados com os dígitos calculados
# Compares the input digits with the calculated digits
def is_valid_cpf(cpf, first_digit, second_digit):
    return int(cpf[9]) == first_digit and int(cpf[10]) == second_digit


# Loop principal do programa
# Main program loop
def run_cpf_validator():
    while True:
        cpf = input('Enter your CPF (numbers only): ')

        if not is_valid_cpf_format(cpf):
            print('Invalid format. Please enter exactly 11 numeric digits.')
            continue

        first_digit = calculate_first_digit(cpf)
        second_digit = calculate_second_digit(cpf)

        if is_valid_cpf(cpf, first_digit, second_digit):
            print(f'{cpf} is a valid CPF.')
        else:
            print(f'{cpf} is not a valid CPF.')

        while True:
            try_again = input('Do you want to check another CPF? [Y]es or [N]o: ').strip().lower()

            if try_again.startswith('y'):
                break
            elif try_again.startswith('n'):
                print('Goodbye!')
                return
            else:
                print('Invalid option. Please type [Y] or [N].')


# Inicia o validador
# Starts the validator
run_cpf_validator()
