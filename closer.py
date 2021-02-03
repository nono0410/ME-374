# Given reference angle and two angles --> Return closer one
import math as m

def closer(ref,prev,test):
    ref = round(ref,3)
    prev = round(prev,3)
    test = round(test,3)
    
    if abs(prev-ref) <= abs(test-ref): # If previous is closer or same
        return prev
    else:
        return test
