
new_list=[]  # storing elemtns
list2=[]  # list for mutiple iteam
list1 = []  # list fro single iteam
Tuple_list = []  # finsl list
 
n1=int(input("Enter the number of tuples::"))

for count, i in enumerate(range(n1)):
    n2=int(input("\nEnter the number of elemment in tuple::"))
    print("\nEnter element in tuple :: ")

    if n2 == 1:
    	b = input('\nEnter the value :: ')
    	new_list.append(b)

    else:

	    for j in range (n2):

	        a = input(f'Enter the value {j + 1} :: ')
	        list2.append(a)
	        list3 = list2[:]
	    new_list.append(tuple(list3))
	    list2.clear()

new_tuple = tuple(new_list)

print('\nThe Tuple is :: ', new_tuple)

for i in range(len(new_tuple)):
	if type(new_tuple[i]) == tuple:
		continue
	else:
		Tuple_list.append(new_tuple[i])

final_tuple = tuple(Tuple_list)

print('\n\nThe Final tuple is :: ', final_tuple)


# Method 2nd

new_list=[]  # storing elemtns
list2=[]  # list for mutiple iteam
list1 = []  # list fro single iteam
Tuple_list = []  # finsl list
 
n1=int(input("Enter the number of tuples::"))

for count, i in enumerate(range(n1)):
    n2=int(input("\nEnter the number of elemment in tuple::"))
    print("\nEnter element in tuple :: ")

    if n2 == 1:
    	b = input('\nEnter the value :: ')
    	new_list.append(b)

    else:

	    for j in range (n2):

	        a = input(f'Enter the value {j + 1} :: ')
	        list2.append(a)
	        list3 = list2[:]
	    new_list.append(tuple(list3))
	    list2.clear()

new_tuple = tuple(new_list)

print('\nThe Tuple is :: ', new_tuple)


for i in range(len(new_tuple)):
	if len(new_tuple[i]) == 1:
		Tuple_list.append(new_tuple[i])

final_tuple = tuple(Tuple_list)

print('\n\nThe Final tuple is :: ', final_tuple)
