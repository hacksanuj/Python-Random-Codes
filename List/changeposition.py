raw_list = []

val = int(input('Enter the limit of list :: '))
print()

for count, i in enumerate(range(val)):
	value = int(input(f'Enter the value {count + 1} :: '))
	raw_list.append(value)

print('\nThe original is :: ', raw_list)

print()
if len(raw_list) % 2 == 0:
	for a in range(0, len(raw_list), 2):
		raw_list[a], raw_list[a + 1] = raw_list[a + 1], raw_list[a] 


	print('The change position list is :: ', raw_list)

else:
	for a in range(0, len(raw_list) - 1, 2):
		raw_list[a], raw_list[a + 1] = raw_list[a + 1], raw_list[a] 
	print('The change position list is :: ', raw_list)