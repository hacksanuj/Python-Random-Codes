def bubble_sort(bubble_list):
	print('\n<<<<<<<<<<<<<<< This is Bubble Sorting >>>>>>>>>>>>>>>')
	length = len(bubble_list)

	for i in range(length):
		for j in range(length - i - 1):

			if bubble_list[j] > bubble_list[j + 1]:
				bubble_list[j], bubble_list[j + 1] = bubble_list[j + 1], bubble_list[j]

	print('\nThe sorted list is :: ', bubble_list)



def inserction_sort(inserction_list):
	print('\n<<<<<<<<<<<<<<< This is Insertion Sorting >>>>>>>>>>>>>>>')
	length = len(inserction_list)

	for i in range(1, length):
		key = inserction_list[i]

		j = i - 1

		while j >= 0 and key < inserction_list[j]:
			inserction_list[j + 1] = inserction_list[j]
			j -= 1
        
        #placing key after smaller ele
		inserction_list[j + 1] = key

	print('\nThe sorted list is :: ', inserction_list)



def selection_sort(selection_list):
	print('\n<<<<<<<<<<<<<<< This is Selection Sorting >>>>>>>>>>>>>>>')
	length = len(selection_list)

	for i in range(length):
		min_val = i

		for j in range(i + 1, length):
			if selection_list[min_val] > selection_list[j]:  # selecting the minimum element
				min_val = j
        
        # swapping element with minimum ele
		selection_list[i], selection_list[min_val] = selection_list[min_val], selection_list[i]

	print('\nThe sorted list is :: ', selection_list)	


def default(def_list):
	print(f'You have entered wrong choice so {def_list} cannot be sorted')


def dict_switch(choice):
	raw_dict = {
      1 : bubble_sort,
      2 : inserction_sort,
      3 : selection_sort
	}

	return raw_dict.get(choice, default)(raw_list)


raw_list = []
value = int(input('Enter the number of values in list :: '))

for i in range(value):
	list_val = int(input(f'Enter the value {i + 1} in list :: '))
	raw_list.append(list_val)

print('\nThe list is :: ', raw_list)


print("""
	1. Enter ->1<- for BUBBLE SORTING
	2. Enter ->2<- for INSERTION SORTING
	3. Enter ->3<- for SELECTION SORTING""")

choice = int(input('\nEnter your Choice ::'))
dict_switch(choice)
