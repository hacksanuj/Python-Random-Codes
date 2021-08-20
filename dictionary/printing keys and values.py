dict_raw = {}

val = int(input('How many key/value pairs you want :: '))
print()

for count, i in enumerate(range(val)):
	key = input(f'Enter the key {count + 1} :: ')
	value = input(f'Enter the value for key {count + 1} :: ')
	dict_raw.update({key : value})
	print()


print('\nThe dictionary is :: ', dict_raw)

print('\n\nIteration of keys :: ')


for count, x in enumerate(dict_raw):
	print(f'The key {count + 1} is :: ', x)

print('\nIteration of values :: ')


for count, x in enumerate(dict_raw):
	print(f'The value at key {count + 1} is :: ', dict_raw[x])

print('\nIteration of keys and values together ::')

for x, y in dict_raw.items():
	print(f'For key :: {x}', end = ' ')
	print(f'value is :: {y}')
