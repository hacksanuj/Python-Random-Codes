raw_list = []

val = int(input('Enter the limit of list :: '))
print()

for count, i in enumerate(range(val)):
	list_val = int(input(f'Enter value {count + 1} in list :: '))
	raw_list.append(list_val)

print('The list is :: ', raw_list)

#sorting of list in ascending order list
raw_list.sort()
print('\nSorted list :: ', raw_list)

sec_val = 0
for x in range(len(raw_list)):
	if raw_list[x] == raw_list[x + 1]:
		continue
	else:
		sec_val = raw_list[x + 1]
		break


print('The second smallest number in list is :: ', sec_val)
