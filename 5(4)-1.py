import random
first_list = ['one', 'two', 'three', 'four', 'five']
second_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
third_list = ['winter', 'spring', 'summer', 'autumn']
list_of_string_list = [first_list, second_list, third_list]

def random_phrase():
    result_string = ""
    for i in range(0,3):
        random_index = random.randrange(0,7)
        result_string = result_string + list_of_string_list[i][random_index] + " "

    return result_string

print(random_phrase())
