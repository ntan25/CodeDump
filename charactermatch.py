# two lists, list 1 and list 2 

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = [1, 2, 3, 4, 5, 6, 7, 9]

newlist = []


for i in range(0, len(list_1) + 1): 
    a = list_1[i]
    b = list_2[i]
    if a != b: 
        newlist.append('*')
    else: 
        newlist.append(a)

print(newlist)
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = [1, 2, 3, 4, 5, 6, 7, 9]

newlist = []


for i in range(0, len(list_1) + 1): 
    a = list_1[i]
    b = list_2[i]
    if a != b: 
        newlist.append('*')
    else: 
        newlist.append(a)

print(newlist)

