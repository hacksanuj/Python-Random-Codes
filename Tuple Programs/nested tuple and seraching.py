def checkTuple(tupl_val, search):
	for i in tupl_val:
		if search in i:
			print(f'\nThe value ->{search}<- is present in tuple')
			break
		else:
			print(f'\nThe value ->{search}<- is not present in tuple')


val_list = []
copy_list = []
new_list = []
value = int(input('Enter the number of nested tuple :: '))

for count, i in enumerate(range(value)):
	nest_val = int(input(f'\nHow many value you want in tuple {count + 1} :: '))
	print('\nEnter the values in tuple ::')

	for count1, j in enumerate(range(nest_val)):
		tup_val = input(f'Enter the value {count1 + 1} :: ')
		val_list.append(tup_val)
		copy_list = val_list[:]
	new_list.append(tuple(copy_list))
	val_list.clear()

new_tuple = tuple(new_list)

print('\nThe nested tuple is :: ', new_tuple)

search_val = input('\nEnter the value which you want to search :: ')

checkTuple(new_tuple, search_val)
