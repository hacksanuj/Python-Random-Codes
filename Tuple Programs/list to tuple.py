str_values = input('Enter the values with comma :: ')

print('\nThe values are :: ', str_values)

val_list = str_values.split(',')  # converting string into list
print('\n\nThe list is :: ', val_list)

val_tuple = tuple(val_list)  # converting list into tuple
print('\nThe tuple is :: ', val_tuple)
