import sys

numbs = sys.argv
numbs.pop(0)

for item in numbs:
    if int(item) % 3 == 0 and int(item) % 5 == 0:
        print("fizzbuzz")
    elif int(item) % 3 == 0:
        print("fizz")
    elif int(item) % 5 == 0:
        print("buzz")
    else:
        print(int(item))