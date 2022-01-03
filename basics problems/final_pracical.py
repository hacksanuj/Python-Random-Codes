def factioral_recursive(r_value):
    if r_value < 0:
        return print('\n\nThe number is negative, So no factorial exist')
        exit
    if r_value == 1 or r_value == 0:
        return 1

    else:
        return r_value * factioral_recursive(r_value - 1)


def factorial_non_rcursive(nr_value):
    print('\n\n************************************************')
    print('\nThis is factorial using non-recursive method :: ')
    fact = 1

    if nr_value < 0:
        print(f'\nSorry the number {nr_value} is negative, So factorial not exist')
        print(f'\n\nThe Factorial of number {nr_value} is :: None')

    elif nr_value == 0:
        print(f'\nThe number {nr_value} Factorial is :: ', fact)

    else:
        for i in range(1, nr_value + 1):
            fact *= i

        print(f'\nThe Factorial of number {nr_value} is :: ', fact)


value = int(input('Enter the value which you want to get the factorial :: '))  # entering value

result = factioral_recursive(value)  # calling recursive function
print('\nThis is factorial using recursive method ')
print(f'\nThe Factorial of number {value} is :: ', result)

factorial_non_rcursive(value)  # calling non recursive function

