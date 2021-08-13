def pal(string):
    if(string == string[::-1]):
        return True
    else:
        return False

def sort_pal(sentence):
    new_list = []
    str_list = list(sentence.split())
      
    for i in str_list:
        if(pal(i)):
            new_list.append(i)
  
    new_list.sort()  # alphabitc sorting

    newlist_index = 0
      
    for i in range(len(str_list)):
        if(pal(str_list[i])):
            str_list[i] = new_list[newlist_index]
            newlist_index = newlist_index + 1

    print('\nThe new string is :: ')
    for i in str_list:
        print(i, end =" ")

sentence = input('Enter the scentence :: ')
sort_pal(sentence)
