from Data import Data
from Net import Net

import torch
import torch.nn as nn
import torch.optim as optim



def train_network(net, dataset):
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    
    for epoch in range(2):
        running_loss = 0.0
        
        for i, data in enumerate(dataset.trainloader, 0):
            #get the imputs
            inputs, labels = data
            
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
                
                
def test_network(net, dataset):
    correct = 0
    total = 0
    
    with torch.no_grad():
        for data in dataset.testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
    print('Accuracy of the network on the 10000 test images: %d %%' %(100 * correct / total))
            
      
##########################################################################################################
    
      
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

dataset = Data()
net = Net()

#use the gpu

train_network(net, dataset)
test_network(net, dataset)




    
    

