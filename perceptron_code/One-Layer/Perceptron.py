import numpy as np
import random
from math import e


class Perceptron(object):
    
    #class constructor
    def __init__(self, input_size = 2, learning_rate = 0.1, epochs = 100):
        self.weight = np.random.rand(input_size + 1)   #bias will be accounted for in the weight and input vectors rather than separately
        self.learning_rate = learning_rate
        self.epochs = epochs



    #Defintion of the activation function ---- CURRENTLY A SIGMOID FUNCTION
    def activation_function(self, input):
       return 1/(1 + e**-input)    #for binary results > 0.5 = 1 ; < 0.5 = 0
       
       
    
    #recieves an input vector and processes it, returning the results
    def prediction(self, input): 
        
        result = self.weight.dot(input)       
        output_result = self.activation_function(result)
        
        return output_result
    
    
    
    #function accepts the all the inputs and desired outputs that will be used to train the perceptron
    #all_inputs may be 1D or 2D depending on how much data you are training it with
    #For example, for a logical function such as AND, each row would contain your pair of binary inputs 
    
    def train(self, all_inputs, desired_outputs):
        
        inputs = np.insert(all_inputs, 0, 1, axis=1)      #inserts 1 at the 0th index of each row (incorporate  bias)
        
        #loop to train the perceptron the number of times specified
        for training_session in range(self.epochs):
            
            #get result of each input (1 row in all_inputs)
            for index in range(desired_outputs.shape[0]):
                result = self.prediction(inputs[index])
                grad_descent = -2 * (desired_outputs[index] - result) * inputs[index]

                new_weight = self.weight - self.learning_rate * grad_descent 
                self.weight = new_weight
            
            
    
    #all_inputs may be a 1D or 2D array
    def test(self, all_inputs):
        
        inputs = np.insert(all_inputs, 0, 1, axis=1) 
        results = np.zeros(all_inputs.shape[0])
        
        for index in range(all_inputs.shape[0]):
            results[index] = self.prediction(inputs[index])
            
        return results