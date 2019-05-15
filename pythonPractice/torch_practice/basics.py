import numpy as np
import torch

"""
###################################################################
NOTES:
-operations that mutate a tensor in place is post-fixed with _
-NumPy array indexing and slicing can be used on tensors as well


##################################################################
"""


#converting between numpy arrays and tensors
#the arrays and tensors share the same data, this just changes how you can interact with it
"""
#create numpy array, use it to create a tensor
#the two data structures share the data, so changes in one will be reflected in both
array = np.ones([5, 6])
print(array)

tensor = torch.from_numpy(array)
print(tensor)

tensor = torch.zeros(3)
print(tensor)
array = tensor.numpy()
print(array)
"""


#creating new tensors
"""
#This shows that the data is shared between the two structures
array += 1

print(array)
print(tensor)

tensor += 1

print(array)
print(tensor)


#tensors can also be initialized in similar ways to arrays

tensor1 = torch.empty(2,8)
print(tensor1)

tensor1 = torch.rand(2,8)
print(tensor1)

tensor1 = torch.zeros(2,8)
print(tensor1)
"""
tensor1 = torch.tensor([2, 8])
print(tensor1)
"""
#create new tesor from existing tensor

tensor1 = tensor1.new_ones(2,5)
print(tensor1)

tensor1 = torch.randn_like(tensor1,dtype=torch.float)
print(tensor1)
"""


#getting sizes of tensors and of various dimensions
"""
print(tensor1.size())

#size() produces a tuple (apparently tuple operations should be supported)
t = tensor1.size()
print(t)

#get a list of the sizes of the dimensions 
l = list(tensor1.size())
print(l)

print(tensor1.shape)

#get the size of each dimension individually
print(tensor1.shape[0])
print(tensor1.shape[1])
"""


#mathematical operations on tensors
"""
#creating some tensors to use
tensor1 = torch.zeros(2,8)
tensor2 = torch.ones(2,8)

tensor3 = torch.add(tensor1, tensor2)
print(tensor3)

tensor4 = torch.empty_like(tensor3)
torch.add(tensor2, tensor3, out=tensor4)   #the out tensor must exist as a tensor before being used here
print(tensor4)

tensor4.add_(tensor3)     #tensor4.add(tensor3) does not do the same as this line
print(tensor4)
"""



