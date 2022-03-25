print(":::::::::::::With 2 variables::::::::::::")

print("\nBEFORE SWAPPING")
num1 = int(input("\n\nEnter number 1::"))
num2 = int(input("Enter the number 2::"))

num1= num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("\nAFTER SWAPPING")

print("\n\nThe number 1 is::", num1)
print("The number 2 is::",num2)


print("\n\n\n:::::::::::With XOR operator::::::::::::")


print("\nBEFORE SWAPPING")
num_01 = int(input("\n\nEnter number 1::"))
num_02 = int(input("Enter the number 2::"))

num_01 = num_01 ^ num_02
num_02 = num_01 ^ num_02
num_01 = num_01 ^ num_02

print("\nAFTER SWAPPING")

print("\n\nThe number 1 is::", num_01)
print("The number 2 is::",num_02)