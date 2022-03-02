raw_list = []

val = int(input('Enter the limit of tuple :: '))
print()

for count, i in enumerate(range(val)):
    value = input(f'Enter the value {count + 1} :: ')
    raw_list.append(value)

raw_tuple = tuple(raw_list)
print('\nThe Tuple is :: ', raw_tuple)

print('\nTuple after removing duplicate elements :: ', tuple(set(raw_tuple)))

# Simple logic

raw_list = []
needed_list = []

val = int(input('Enter the limit of tuple :: '))
print()

for count, i in enumerate(range(val)):
    value = input(f'Enter the value {count + 1} :: ')
    raw_list.append(value)

for i in raw_list:
    if i not in needed_list:
        needed_list.append(i)

print('\nThe Tuple is :: ', tuple(needed_list))
