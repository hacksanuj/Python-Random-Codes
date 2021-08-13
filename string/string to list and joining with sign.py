String = input("Enter any string::") #input in string

newString = String.split()  # used split() method to break string into list
print('\nSpliting the String inro list::', newString)  # printing the list of string

new_string = '-'.join(newString) #joining the list of string with - sign

print('\nString after joining the sign - :: ', new_string)  #printing the joined string
