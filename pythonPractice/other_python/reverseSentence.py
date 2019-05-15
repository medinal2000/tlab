#reverses a given sentence
def reverse_sentence (sentence):
    split_string = sentence.split()
    split_string.reverse()
    
    return split_string


sentence = "How are you ?"
r_sentence = reverse_sentence(sentence)

print (str(r_sentence))

