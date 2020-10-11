# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME
import numpy as np
class DynamicArray:
    data = np.empty(0)
    pass
    def __init__(self):
        self.capacity = 10
        self.length = 0
        self.data = np.empty(self.capacity, object)
    
    def __len__(self):
        return self.length

    def is_empty(self):
        if self.length == 0:
            return True
        return False
    
    def append(self,num):
        self.data = np.array([num])

    def __getitem__(self, index):
        return self.data[index]