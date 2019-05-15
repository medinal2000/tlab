#function to find the divisors of a number
def find_divisors(number):
    divisors = []

    for i in range(1, number+1):
        if number%i == 0:
            divisors.append(i)
            
    return divisors
                
                
number = int(input("Please enter a number: "))


#find divisors for number entered

divisors = find_divisors(number)        
print ("These are the divisors of", number, ": ", divisors)


#is number prime?

if len(divisors) < 3:
    print(number, "is prime")
else:
    print(number,"is not prime")