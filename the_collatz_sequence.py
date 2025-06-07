# The Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result

while True:
    try:
        number = input('Enter a number: ')
        number = int(number)
        # Added a check for positive numbers as the Collatz sequence is typically defined for positive integers.
        if number <= 0:
            print('Please enter a positive number.')
            continue # Continue the loop to ask for input again
        break
    except ValueError: # Catching specific ValueError
        print('Enter a valid integer.')
    except Exception as e: # Catching any other unexpected errors
        print(f"An unexpected error occurred: {e}")

while number != 1:
    number = collatz(number)