raw_list = []

val = int(input('Enter the limit of tuple :: '))
print()

for count, i in enumerate(range(val)):
    value = input(f'Enter the value {count + 1} :: ')
    raw_list.append(value)

raw_tuple = tuple(raw_list)
print('\nThe Tuple is :: ', raw_tuple)

tuple_val = input('\nEnter the value which you want to check :: ')

if tuple_val in raw_tuple:
    print(f'\nThe value :: ->{tuple_val}<- is present in tuple.')
else:
    print(f'\nThe value :: ->{tuple_val}<- is not present in tuple.')