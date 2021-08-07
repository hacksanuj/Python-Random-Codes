res_list = []

string = input('Enter the string :: ')
new_str = string.split()

print('\nThe string list is :: ', new_str)

length = int(input('\nEnter the length to check :: '))

for i in new_str:
	if len(i) > length:
		res_list.append(i.upper())
	else:
		res_list.append(i)

print('\n final string is :: ',res_list)
