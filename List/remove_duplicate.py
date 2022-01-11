new_list=[]
list2=[]
n1=int(input("Enter the number of list in list::"))
for count, i in enumerate(range(n1)):
    n2=int(input(f"\nEnter the number of elemment in list {count + 1} ::"))
    print(f"\nEnter element in list {count + 1} :: ")
    for j in range (n2):

        a = int(input(f'Enter the value {j + 1} :: '))
        list2.append(a)
        list3 = list2[:]
    new_list.append(list3)
    list2.clear()
print('\nThe lists of list is :: ', new_list)

no_dul_list = []

for i in new_list:
	if i not in no_dul_list:
		no_dul_list.append(i)

print('\nList after removing duplicate lists :: ', no_dul_list)