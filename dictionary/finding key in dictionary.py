dict_raw = {}

val = int(input('How many key/value pairs you want :: '))
print()

for count, i in enumerate(range(val)):
	key = input(f'Enter the key {count + 1} :: ')
	value = input(f'Enter the value for key {count + 1} :: ')
	dict_raw.update({key : value})
	print()


print('\nThe dictionary is :: ', dict_raw)

val_key = input('\nEnter the key value which you want to search :: ')

if val_key in dict_raw.keys():
	print('\nThe key is present')
	print('The value of key is :: ', dict_raw.get(val_key))
else:
	print('\nThe key is not present')