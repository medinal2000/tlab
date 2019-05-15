list = [1,2,3,4,5,6,7,8,9]

#printing all the numbers in the list that are less than 5


#way 1
for num in list:
    if num < 5:
        print(num)
        
#way 2
lessThanFive = []

for num in list:
    if num < 5:
        lessThanFive.append(num)
        
for num in lessThanFive:
       print(num)
        
print (lessThanFive)