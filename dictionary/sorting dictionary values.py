dict_raw = {}

val = int(input('How many key/value pairs you want :: '))
print()

for count, i in enumerate(range(val)):
	key = input(f'Enter the key {count + 1} :: ')
	value = int(input(f'Enter the value for key {count + 1} :: '))
	dict_raw.update({key : value})
	print()

print('\nThe dictionary is :: ', dict_raw)

print('''\n1.To sort in Ascending order enter :: asc
2.To sort in Descending order enter :: desc''')

choice = input('\nEnter the choice::')

if choice == 'asc':
	sorted_dict = {}
	list1 = list(dict_raw.values())
	list1.sort()

	print('\nThe sorted keys values are :: ', list1)

	for i in list1:
	    for j in dict_raw.keys():
	        if dict_raw[j] == i:
	            sorted_dict[j] = dict_raw[j]
	            break

	print('\nThe sorted list ::', sorted_dict)

else:
	sorted_dict = {}
	list1 = list(dict_raw.values())
	list1.sort(reverse = True)

	print('\nThe sorted keys values are :: ', list1)

	for i in list1:
	    for j in dict_raw.keys():
	        if dict_raw[j] == i:
	            sorted_dict[j] = dict_raw[j]
	            break

	print('\nThe sorted list ::', sorted_dict)
