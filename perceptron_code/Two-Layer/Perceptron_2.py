import numpy as np
import random
from math import e

###################################################
# This is has 1 hidden layer and 1 output layer
# Hidden layer has 2 nodes, output layer has 1 node
###################################################

class Perceptron(object):
    
    #class constructor
    def __init__(self, learning_rate = 0.01, epochs = 10000):
        #input sizes for different layers, including 1 more to include bias
        input_size_h = 3
        input_size_o = 3 
        
        #hidden weights
        self.weight_h1 = np.random.rand(input_size_h)
        self.weight_h2 = np.random.rand(input_size_h)
        
        #output weights
        self.weight_o = np.random.rand(input_size_o)
       
        self.learning_rate = learning_rate
        self.epochs = epochs



    #Defintion of the activation function ---- CURRENTLY A SIGMOID FUNCTION
    def activation_function(self, x, deriv = False):
        if deriv == True:
            return x * (1 - x)
        else:
            return 1/(1 + e**-x)    #for binary results >= 0.5 = 1 ; < 0.5 = 0
        
        
    
    #recieves an input vector and processes it, returning the results
    def prediction(self, input):
        #result array to hold results of hidden layer
        result_h = np.empty_like(self.weight_o)
       
        all_nodes_results = np.empty_like(self.weight_o)
        
        #1 for the bias at 0th index
        result_h[0] = 1
        
        #put input through the hidden nodes
        result_h[1] = self.activation_function(self.weight_h1.dot(input))
        all_nodes_results[0] = result_h[1]
        
        result_h[2] =  self.activation_function(self.weight_h2.dot(input))
        all_nodes_results[1] = result_h[2]
 
        #process inputs into output node          
        result = self.weight_o.dot(result_h)
        all_nodes_results[2] = self.activation_function(result)
        
        return all_nodes_results
    
    
    
    #implements back propagation for the neural network
    def back_prop(self, output_h1, output_h2, actual_output, desired_output, inputs):
                
        loss_derivative = -2 * (desired_output - actual_output)
        
        #output layer
        grad_descent_o = np.empty_like(self.weight_o)
        
        grad_descent_o[0] = loss_derivative * 1          #bias always multiplied by 1
        grad_descent_o[1] = loss_derivative * output_h1
        grad_descent_o[2] = loss_derivative * output_h2
        
        #hidden layers
        grad_descent_h1 = loss_derivative * self.weight_o[1] * self.activation_function(output_h1, deriv = True) * inputs        
        grad_descent_h2 = loss_derivative * self.weight_o[2] * self.activation_function(output_h2, deriv = True) * inputs 
     
        #update weights
        self.weight_o -= self.learning_rate * grad_descent_o
        self.weight_h1 -= self.learning_rate * grad_descent_h1 
        self.weight_h2 -= self.learning_rate * grad_descent_h2
        
    
    
    #function accepts the all the inputs and desired outputs that will be used to train the perceptron
    #all_inputs may be 1D or 2D depending on how much data you are training it with
    #For example, for a logical function such as AND, each row would contain your pair of binary inputs
    def train(self, all_inputs, desired_outputs):
        
        inputs = np.insert(all_inputs, 0, 1, axis=1)#inserts 1 at the 0th index of each row (incorporate  bias)
        
        #loop to train the perceptron the number of times specified
        for training_session in range(self.epochs):
            
            #get result of each input (1 row in all_inputs)
            for index in range(desired_outputs.shape[0]):
                results = self.prediction(inputs[index])
                self.back_prop(results[0], results[1], results[2], desired_outputs[index], inputs[index])
            
                               
    
    #all_inputs may be a 1D or 2D array
    def test(self, all_inputs):
        
        inputs = np.insert(all_inputs, 0, 1, axis=1) 
        results = np.zeros(all_inputs.shape[0])
        
        for index in range(all_inputs.shape[0]):
            results[index] = self.prediction(inputs[index])[2]
            
        return results
