# import caesarcipher as cs


plain_text = input('Enter the plain text :: ')
value = int(input('\nEnter the shift :: '))

hello = cs.CaesarCipher(plain_text ,offset = value)
print('\n\nThe encripted string is ::', end = ' ')
print(hello.encoded)



# simple method without libries

small_alpha = 'abcdefghijklmnopqrstuvwxyz'
capital_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''


str_val = input('Enter the text here :: ')

print('\n1. For encription in forward dicrection \n2. For encription in backword direction')

choice = int(input('\nEnter you choice ::'))

if choice == 1:
	shift = int(input('\nEnter the shift :: '))

	for i in str_val:

		if i in small_alpha:
			result += small_alpha[(small_alpha.index(i) + shift) % len(small_alpha)]

		elif i in capital_alpha:
			result += capital_alpha[(capital_alpha.index(i) + shift) % len(capital_alpha)]

		else:
			result += ' '

	print(result)

else:
	shift = int(input('\nEnter the shift :: '))

	for i in str_val:

		if i in small_alpha:
			result += small_alpha[(small_alpha.index(i) - shift) % len(small_alpha)]

		elif i in capital_alpha:
			result += capital_alpha[(capital_alpha.index(i) - shift) % len(capital_alpha)]

		else:
			result += ' '

	print(result)


	
