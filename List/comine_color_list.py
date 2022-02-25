list1 = []

val1 = int(input('Enter the limit of list 1 :: '))
print()

for count, i in enumerate(range(val1)):
	list_val1 = input(f'Enter value {count + 1} in list :: ')
	list1.append(list_val1)

print('The list 1 is :: ', list1)

list2 = []

val2 = int(input('\n\nEnter the limit of list 2 :: '))
print()

for count, i in enumerate(range(val2)):
	list_val2 = input(f'Enter value {count + 1} in list :: ')
	list2.append(list_val2)

print('The list is :: ', list2)

print('\nthe combined list is ::;' )

new_list = []
for i in range(len(list1)):
	new_list.append({list1[i]:list2[i]})
	
print(new_list)