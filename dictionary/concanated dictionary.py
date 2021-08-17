x = int(input('how many dictionary you want :: '))
dict_raw = {}

for count, x in enumerate(range(x)):
	dict_raw[x] = {}

	val = int(input(f'\nHow many key/value pairs you want in dictionary {count + 1} :: '))
	print()

	for count, i in enumerate(range(val)):
		key = input(f'Enter the key {count + 1} :: ')
		value = input(f'Enter the value for key {count + 1} :: ')
		dict_raw[x].update({key : value})
		print()


	print(f'\nThe dictionary {count + 1} is :: ', dict_raw[x])

print('The concanated dictionary is :: ', dict_raw)


#################################################################################################################################

dict1={
    1:"Pheonix",
    2:"Duelist"
}
dict2={
    3:"Jett in",
    4:"Valorant"
}
print(f"First dictionary is :: {dict1}")
print(f"Second dictionary is :: {dict2}")
dict1.update(dict2)
print(f"Concated dictionary is {dict1}")


#merging
needed_dict = dict1.copy()
needed_dict.update(dict2)

print(f'\n The merge dictionary is :: {needed_dict}')

