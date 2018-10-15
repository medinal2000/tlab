import numpy as np
from Perceptron import Perceptron
    
#########################TRAIN PERCEPTRONS##########################################    
#this will not be changed in this program
all_inputs = np.array([    
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ])


#code for AND
                
and_perceptron = Perceptron(input_size = 2)

desired_output = np.array([0,0,0,1])

and_perceptron.train(all_inputs, desired_output)



#code for OR

or_perceptron = Perceptron(input_size = 2)

desired_output = np.array([0,1,1,1])

or_perceptron.train(all_inputs, desired_output)
              
              
              
#code for XOR

xor_perceptron = Perceptron(input_size = 2)

desired_output = np.array([0,1,1,0])

xor_perceptron.train(all_inputs, desired_output)


    
###############################TEST PERCEPTRONS#########################################

#Same order of data used to train the perceptrons
results = and_perceptron.test(all_inputs)
print(results)

results = or_perceptron.test(all_inputs)
print(results)

results = xor_perceptron.test(all_inputs)
print(results)


