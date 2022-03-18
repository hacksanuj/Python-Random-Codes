a = int(input("Enter the marks in 1 out of 100::"))
b = int(input("Enter the marks in 2 out of 100::"))
c = int(input("Enter the marks in 3 out of 100::"))
d = int(input("Enter the marks in 4 out of 100::"))
e = int(input("Enter the marks in 5 out of 100::"))

total = a+b+c+d+e
avg = total / 5
per = (total / 500) * 100
print("\nTOTAL  MARKS::", total)
print("\nAverage of marks::",float(avg))
print("percentage::",float(per))