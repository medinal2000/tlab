import torch

###################################################
# This is has 1 hidden layer and 1 output layer
# Hidden layer has 2 nodes, output layer has 1 node
###################################################

class Perceptron(object):
    
    #class constructor
    def __init__(self, learning_rate = 0.01, epochs = 10000):

        input_dimension = 2          #number of inputs at a time
        output_dimension = 1         #number of outputs per set of inputs 
        num_hidden = 2               #number of hidden nodes 
             
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.hidden_weight = torch.randn(input_dimension + 1, num_hidden, dtype=torch.float, requires_grad=True)
        self.output_weight = torch.randn(num_hidden + 1, output_dimension, dtype=torch.float, requires_grad=True)


    def append_ones(self, all_inputs):
        inputs = torch.empty(all_inputs.size()[0], all_inputs.size()[1] + 1)             #batch_size, input_dimension + 1
        
        for i in range(inputs.size()[0]):
            for j in range(inputs.size()[1]):
                if j == inputs.size()[1] - 1:
                    inputs[i][j] = 1
                else:
                    inputs[i][j] = all_inputs[i][j]
            
        return inputs
                
 
    #recieves an input vector and processes it, returning the results
    def forward(self, input):
        
        #pass inputs through the hidden layer
        hidden_output = torch.mm(input, self.hidden_weight)   #output of hidden layer before being squished by activation function; this is matrix multiplication!
        hidden_output = torch.sigmoid(hidden_output)
        
        hidden_output = self.append_ones(hidden_output)
        
        #pass through the output layer to get the final output of the network
        actual_output = torch.mm(hidden_output, self.output_weight)   #output of output layer before being squished by activation function
        actual_output = torch.sigmoid(actual_output)
            
        return actual_output
 
    
    #function accepts the all the inputs and desired outputs that will be used to train the perceptron
    #all_inputs may be 1D or 2D depending on how much data you are training it with; USE AS IS
    #For example, for a logical function such as AND, each row would contain your pair of binary inputs
    def train(self, all_inputs, desired_outputs):
        inputs = self.append_ones(all_inputs)
        
        #loop to train the perceptron the number of times specified
        for training_session in range(self.epochs):
            actual_output = self.forward(inputs)
            loss = torch.sum((desired_outputs - actual_output)**2) / 4
            
            #backprop
            loss.backward()
           
            with torch.no_grad():
                #update the weights
                self.hidden_weight += self.learning_rate * self.hidden_weight.grad
                self.output_weight += self.learning_rate * self.output_weight.grad
                
               #reset gradients to 0
                self.hidden_weight.grad.zero_()
                self.output_weight.grad.zero_()
             
    
    #all_inputs may be a 1D or 2D array; USE AS IS
    def test(self, all_inputs):
        
        inputs = self.append_ones(all_inputs) 
        results = self.forward(inputs)    
            
        return results
