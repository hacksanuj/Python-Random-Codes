def stringchar(a, b):
	new_a = b[:-1] + a[-1]
	new_b = a[:-1] + b[-1]
	return new_a + ' ' + new_b


string_01 = input('Enter the first string :: ')
string_02 = input('Enter the second string :: ')

str1 = string_01.replace(" ", "")
str2 = string_02.replace(" ", "")

final_string = stringchar(str1, str2)

print('\nThe final string is :: ',final_string)
