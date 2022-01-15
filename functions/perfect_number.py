def perfect_number(num):
	sum = 0
	for i in range(1, num):
		if num % i == 0:
			sum += i

	if sum == num and sum != 0:
		print(f'\nThe number {num} is perfect number')
	else:
		print(f'\nThe number {num} is not perfect number')

number = int(input('Enter the number :: '))
perfect_number(number)