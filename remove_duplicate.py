my_list = [2, 4, 1, 4, 8, 13, 4, 8, 13, 7, 0, 0]
my_new_list =[]
for position in my_list:
    if position not in my_new_list:
        my_new_list.append(position)
print(my_new_list)