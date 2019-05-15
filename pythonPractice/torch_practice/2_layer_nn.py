#######################################################
# Name: 2_layer_nn.py
# Description: Contains the code for a class that can
#              be used to create and test a 2 layer
#              neural network
# Author: Medina Lamkin
# Last Edited: 
#######################################################

import torch
import torch.nn as nn

class Perceptron(object):
    
    #class constructor ; num_hidden specifies the number of hidden nodes in 1 layer
    def __init__(self, input_size = 2, learning_rate = 0.1, epochs = 100):
        #the number of hidden nodes
        self.num_hidden = 2
        
        #bias will be incorporated into the weights vectors
        #might be better to have a matrix of weights for each layer
        self.hidden_weights1 = np.random.rand(input_size + 1)
        self.hidden_weights2 = np.random.rand(input_size + 1)
        self.output_weight = np.random.rand(num_hidden + 1)
        
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
        
            
            
    
    #all_inputs may be a 1D or 2D array
    def test(self, all_inputs):
        
        