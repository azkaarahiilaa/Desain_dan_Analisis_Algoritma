import numpy as np
 
a=[1,2,3]
b=[4,5,6]

def add (list_a, list_b):
    result=[]
    for first, second in zip(list_a, list_b):
        result.append(first+second)
    return result
print (add(a,b))