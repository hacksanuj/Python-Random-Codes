raw_list = []
product = 1
val = int(input('Enter the limit of tuple :: '))
print()

for count, i in enumerate(range(val)):
    value = int(input(f'Enter the value {count + 1} :: '))
    raw_list.append(value)

raw_tuple = tuple(raw_list)
print('\nThe Tuple is :: ', raw_tuple)

for i in range(len(raw_tuple)):
	product *= raw_tuple[i]

print('\nThe product of elements of tuple :: ', product)