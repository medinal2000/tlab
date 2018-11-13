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
                
and_perceptron = Perceptron()

desired_output = np.array([0,0,0,1])

and_perceptron.train(all_inputs, desired_output)



#code for OR

or_perceptron = Perceptron()

desired_output = np.array([0,1,1,1])

or_perceptron.train(all_inputs, desired_output)
              
              
              
#code for XOR

xor_perceptron = Perceptron()

desired_output = np.array([0,1,1,0])

xor_perceptron.train(all_inputs, desired_output)


    
###############################TEST PERCEPTRONS#########################################

#Same order of data used to train the perceptrons
results = and_perceptron.test(all_inputs)
print("End results")
result_b = np.empty_like(results)
for result in range(4):
    if results[result] >= 0.5:
        result_b[result] = 1
    else:
        result_b[result] = 0
print(result_b)
print()
print()
print()

results = or_perceptron.test(all_inputs)
print("End results")
result_b = np.empty_like(results)
for result in range(4):
    if results[result] >= 0.5:
        result_b[result] = 1
    else:
        result_b[result] = 0
print(result_b)
print()
print()
print()

results = xor_perceptron.test(all_inputs)
print("End results")
result_b = np.empty_like(results)
for result in range(4):
    if results[result] >= 0.5:
        result_b[result] = 1
    else:
        result_b[result] = 0
print(result_b)

