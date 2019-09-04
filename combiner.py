# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:29:38 2019

@author: Vader

"""
##### ---------- Combiner function : takes in multiple values or list and return concatenated string values followed by sum of int and float types

#- - - - - 
def combiner(item):
    final = ""
    total = 0
    for i in item:
        if isinstance(i, str):
            final+=i
        elif isinstance(i,(int,float)):
            total+=i
    return final + str(total)


#- - - - - 

def combiner_multiple(*args):
    final=""
    total = 0
    for i in args:
        if isinstance(i, str):
            final+=i
        else:
            total+=i
    return final+str(total)

## Function calls
list_try = [25,'thirteen','item',3.5,34.6,'twentyfive']
combiner(list_try)
combiner_multiple(25,'thirteen','item',3.5,34.6,'twentyfive')
