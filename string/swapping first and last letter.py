#using slicing in string

string = input('Enter the string value :: ')

print('Print new string ::')
print(string[-1] + string[1:-1] + string[0])

# 2nd method
# using replace method

string = input('Enter the string value ::')
last_value = string[-1]
first_value = string[0]

new_string = string.replace(last_value, first_value, 1)

string_new = new_string.replace(first_value,last_value, 1)
print('\nThe Swapped string is :: ' + string_new)

# 3rd method
# spwapping every first and last alphabet of each word in a string

string = input('Enter the value in String ::')

list_string = string.split()
new_list = []

for word in list_string:
	new_list.append(word[-1] + word[1 : -1] + word[0])


new_string = " ".join(new_list)
print(new_string)
