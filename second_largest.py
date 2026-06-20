list = [34, 25, 74, 30, 4, 55]

iteration = 0
while iteration < 2:
    
    for items in list:
        max = list[0]
        if items > max:
            max = items
            list.remove(max)
        iteration += 1
print(max)