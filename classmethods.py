# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:35:52 2019

@author: Vader
"""

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __iter__(self):
        yield from self.pattern
      
    def __str__(self):
        output = []
        for i in self:
            if i == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)
    
    @classmethod
    def from_string(cls, value):
        input_list = value.split('-')
        out_list = []
        for i in input_list:
            if i =='dot':
                out_list.append('.')
            elif i == 'dash':
                out_list.append('_')
        return cls(out_list)

#class S(Letter):
#    def __init__(self):
#         pattern = ['.', '.', '.']
#         super().__init__(pattern)

# Does not print the desired output, but code works magically
#bug
test_one = Letter.from_string('dot-dot')
print(test_one)

