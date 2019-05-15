number = int(input("Tell me a number: "))

if number%4 == 0:
    print("Your number is divisible by 4")

elif number%2 == 0:
    print("Your number is even")

else:
    print("Your number is odd")
    
#checking divisibility of num by check
    
num = int(input("Tell me another number: "))
check = int(input("And a last number: "))

if num%check == 0:
    print(str(num) + " is divisible by " + str(check))
    print(num, " is divisible by ", check)

else:
    print(str(num) + " is not divisible by " + str(check))