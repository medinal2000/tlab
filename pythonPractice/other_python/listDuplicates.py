list1 = ['a','g','r','f','c','s','w','q']
list2 = ['a','y','r','c','g','w']

duplicates = []

for element1 in list1:
    for element2 in list2:
        if element1 == element2:
            duplicates.append(element1)
            
print(duplicates)