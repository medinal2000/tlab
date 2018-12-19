from Data import Data
from Net import Net

import torch.nn as nn
import torch.optim as optim



def train_network(net):
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    
    for epoch in range(2):
        running_loss = 0.0
        
        for i, image in enumerate(data.trainloader, 0):
            #get the imputs
            inputs, labels = image
            
            #zero gradients
            optimizer.zero_grad()
            
            #do the forward and backward passes, then optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            #print running_loss and reset it
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0
            
            

data = Data()
net = Net()

train_network(net)





    
    

