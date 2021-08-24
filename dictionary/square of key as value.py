dict_raw = {}
value = int(input('Enter the value to which you want to generate dictionary :: '))

for i in range(0, value):
	dict_raw.update({i + 1 : (i + 1) * (i + 1)})

print('\nThe dictionary is :: ', dict_raw)
