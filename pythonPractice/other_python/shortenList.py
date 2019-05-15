#makes a new list that only contains the first and last elements
def shorten_list(list):
    new_list = []
    
    if len(list) > 0:
        new_list.append(list[0])
    if len(list) > 1:
        new_list.append(list[len(list) - 1])
        
    return new_list
        

list = [1,2,3,4,5,6,7,8,9,0]

new_list = shorten_list(list)

print(new_list)

