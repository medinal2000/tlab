import numpy as np
import random
from math import e


class Perceptron(object):
    
    #class constructor
    def __init__(self, input_size, learning_rate = 1, epochs = 10):
        self.weight = np.random.rand(input_size + 1)   #bias will be accounted for in the weight and input vectors rather than separately
        self.learning_rate = learning_rate
        self.epochs = epochs


    #Defintion of the activation function ---- CURRENTLY A STEP FUNCTION
    def activation_function(self, input):
       
       
       #sigmoid function
       return 1/(1 + e**-input)
       
       
       #step function
       #if input >= 0:
       #     return 1
        
       #else:
       #    return 0


    
    #recieves an input vector and processes it, returning the results
    def prediction(self, inputs): 
        
        v = self.weight.dot(inputs)         #v is the dot product of the weights and inputs vector
            
        output_result = self.activation_function(v)
        
        return output_result
    
    
    
    #function accepts the all the inputs and desired outputs that will be used to train the perceptron
    #all_inputs may be 1D or 2D depending on how much data you are training it with
    #For example, for a logical function such as AND, each row would contain your pair of binary inputs 
    
    def train(self, all_inputs, desired_outputs):
        
        #loop to train the perceptron the number of times specified
        for training_session in range(self.epochs):
            
            for index in range(desired_outputs.shape[0]):
                inputs = np.insert(all_inputs[index], 0, 1)      #inserts a 1 at the 0th index of each row; this is to incorporate the bias
                result = self.prediction(inputs)
                error = desired_outputs[index] - result
                self.weight = self.weight + self.learning_rate * error * inputs      #adjusting the weight
            
    
    #all_inputs may be a 1D or 2D array
    def test(self, all_inputs):
        results = np.zeros(all_inputs.shape[0])
        
        for index in range(all_inputs.shape[0]):
            inputs = np.insert(all_inputs[index], 0, 1)      #inserts a 1 at the 0th index of each row; this is to incorporate the bias
            results[index] = self.prediction(inputs)
            
        return results
    
