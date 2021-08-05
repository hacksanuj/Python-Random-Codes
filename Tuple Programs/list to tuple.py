str_values = input('Enter the values with comma :: ')

print('\nThe values are :: ', str_values)


 # converting string into list
val_list = str_values.split(',') 
print('\n\nThe list is :: ', val_list)


# converting list into tuple
val_tuple = tuple(val_list)  
print('\nThe tuple is :: ', val_tuple)
