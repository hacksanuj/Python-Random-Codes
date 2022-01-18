def showEmployee(name, sal = 9000):

	print('\nEmployee name is :: ', name)
	print('Employee salary is :: ',sal)

ename = input('Enter the name of employee :: ')
esal = input('\nEnter the salary of employee :: ')


if esal != '':
	showEmployee(ename,esal)
else:
	showEmployee(ename)