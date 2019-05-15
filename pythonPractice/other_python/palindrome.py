word = input("please enter a word\n")

count = 0
palindrome = "true"
maxIndex = len(word) - 1

while count < len(word):
    if word[count] != word[(maxIndex-count)]:
        palindrome = "false"
        
    count +=1
        
print(palindrome)