#import set

#lists
def remove_duplicates(list):
    new_list = []
    
    
    for element1 in list:
        to_add = True
        
        for element2 in new_list:
            if element1 == element2:
                to_add = False
                
        if to_add == True:
                new_list.append(element1)
                
    return new_list


#sets
def list_to_set(list):
    new_set = set([])
    new_set.update(list)
    
    return new_set


list = [1,2,3,4,2,1,3,5,6,7,2]

new_list = remove_duplicates(list)
print(new_list)

new_set = list_to_set(list)
print(new_set)
