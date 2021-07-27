dict_raw = {}

# tuple 1
raw_list1 = []
val = int(input('Enter the limit of 1st tuple :: '))
print()

for count, i in enumerate(range(val)):
    value = input(f'Enter the value {count + 1} :: ')
    raw_list1.append(value)

raw_tuple1 = tuple(raw_list1)
print('\nThe 1st Tuple is :: ', raw_tuple1)


# tuple 2
raw_list2 = []

val = int(input('\nEnter the limit of 2nd tuple :: '))
print()

for count, i in enumerate(range(val)):
    value = input(f'Enter the value {count + 1} :: ')
    raw_list2.append(value)

raw_tuple2 = tuple(raw_list2)
print('\nThe 2nd Tuple is :: ', raw_tuple2)


# dictionary
for i in range(0, len(raw_tuple1)):
	dict_raw.update({raw_tuple1[i]:raw_tuple2[i]})

print('\nThe dictionary is :: ', dict_raw)


##########################################################################################################################################################################


# 2nd method

new_list=[]
list2=[]
n1=int(input("Enter the number of tuples::"))
for count, i in enumerate(range(n1)):
    n2=int(input(f"\nEnter the number of elemment in tuple {count + 1} ::"))
    print(f"\nEnter element in tuple {count + 1} :: ")
    for j in range (n2):

        a = input(f'Enter the value {j + 1} :: ')
        list2.append(a)
        list3 = list2[:]
    new_list.append(tuple(list3))
    list2.clear()

new_tuple = tuple(new_list)

print('\nThe Tuple is :: ', new_tuple)

print('\nThe dictionary is :: ', dict(new_tuple))
