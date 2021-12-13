import random


def quick_first(list_first):
    print('\n<<<<<<<<<< This is quick sort with pivot as first element >>>>>>>>>>')

    def quick_sort(sequence):

        length = len(sequence)
        if length <= 1:
            return sequence
        else:
            pivot = sequence.pop(0)

        ele_greater = []
        ele_smaller = []

        for ele in sequence:
            if ele > pivot:
                ele_greater.append(ele)

            else:
                ele_smaller.append(ele)

        return quick_sort(ele_smaller) + [pivot] + quick_sort(ele_greater)

    result = quick_sort(list_first)
    print('\nThe sorted list is :: ', result)


def quick_last(list_last):
    print('\n<<<<<<<<<< This is quick sort with pivot as last element >>>>>>>>>>')

    def quick_sort(sequence):

        length = len(sequence)
        if length <= 1:
            return sequence
        else:
            pivot = sequence.pop()

        ele_greater = []
        ele_smaller = []

        for ele in sequence:
            if ele > pivot:
                ele_greater.append(ele)

            else:
                ele_smaller.append(ele)

        return quick_sort(ele_smaller) + [pivot] + quick_sort(ele_greater)

    result = quick_sort(list_last)
    print('\nThe sorted list is :: ', result)


def quick_mid(list_mid):
    print('\n<<<<<<<<<< This is quick sort with pivot as middle element >>>>>>>>>>')

    def quick_sort(sequence):

        length = len(sequence)
        if length <= 1:
            return sequence
        else:
            middle = length // 2
            pivot = sequence.pop(middle)

        ele_greater = []
        ele_smaller = []

        for ele in sequence:
            if ele > pivot:
                ele_greater.append(ele)

            else:
                ele_smaller.append(ele)

        return quick_sort(ele_smaller) + [pivot] + quick_sort(ele_greater)

    result = quick_sort(list_mid)
    print('\nThe sorted list is :: ', result)


def quick_random(list_random):
    print('\n<<<<<<<<<< This is quick sort with pivot as random element >>>>>>>>>>')

    def quick_sort(sequence):

        length = len(sequence)
        if length <= 1:
            return sequence
        else:
            rand_pivot = random.randrange(0, length - 1)
            pivot = sequence.pop(rand_pivot)

        ele_greater = []
        ele_smaller = []

        for ele in sequence:
            if ele > pivot:
                ele_greater.append(ele)

            else:
                ele_smaller.append(ele)

        return quick_sort(ele_smaller) + [pivot] + quick_sort(ele_greater)

    result = quick_sort(list_random)
    print('\nThe sorted list is :: ', result)


def default(list_deafult):
    print(f'\nWrong case hence {list_deafult} will not be sorted')


def dict_switch(new_choice):
    raw_dict = {
      1: quick_first,
      2: quick_last,
      3: quick_mid,
      4: quick_random
    }

    return raw_dict.get(new_choice, default)(raw_list)


raw_list = []
value = int(input('Enter the number of values in list :: '))

for i in range(value):
    list_val = int(input(f'Enter the value {i + 1} in list :: '))
    raw_list.append(list_val)

print('\nThe list is :: ', raw_list)


print("""
    1. Enter ->1<- for sorting through first value as pivot
    2. Enter ->2<- for sorting through last value as pivot
    3. Enter ->3<- for sorting through mid value as pivot
    4. Enter ->4<- for sorting through random value as pivot""")

choice = int(input('\nEnter your Choice ::'))
dict_switch(choice)
