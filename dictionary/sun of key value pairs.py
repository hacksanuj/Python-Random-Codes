dict_raw = {}

val = int(input('How many key/value pairs you want :: '))
print()

for count, i in enumerate(range(val)):
	key = int(input(f'Enter the key {count + 1} :: '))
	value = int(input(f'Enter the value for key {count + 1} :: '))
	dict_raw.update({key : value})
	print()

print('\nThe dictionary is :: ', dict_raw)

sum_keys = sum(dict_raw.keys())
sum_values = sum(dict_raw.values())

dict_raw.update({sum_keys : sum_values})

print('\nThe new dictionary is :: ', dict_raw)
