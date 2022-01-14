def recurive_sum(num):
	if num > 10:
		return 0
	else:
		return num + recurive_sum(num + 1)

result = recurive_sum(1)
print('The sum of numbers 0-10 are :: ', result)


