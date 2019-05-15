def ask_user():
    number = int(input("How many Fibonacci numbers would you like to generate? "))
    return number

def generate_fibonnaci(number):
    fibonnaci_nums = []
    
    if number > 0:
       
        if number >= 1:
            fibonnaci_nums.append(1)
            
        if number >= 2:
            fibonnaci_nums.append(1)
            
        if number > 2:
            count = 2
            
            while count < number:
                num_to_add = fibonnaci_nums[count - 1] + fibonnaci_nums[count - 2]
                fibonnaci_nums.append(num_to_add)
                count += 1
            
    return fibonnaci_nums



fibonnaci_nums = generate_fibonnaci(ask_user())

print ("Here are your Fibonnaci numbers: "fibonnaci_nums)
        
            