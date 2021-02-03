# Define points of rectangle
import math as m

#B = O1[0] + O1B*m.cos(a) , O1[1] + O1B*m.sin(a)
#C = B[0] + L*m.sin(t) , B[1] + -1*L*m.cos(t)

# Given point B,angle(alpha),and reference length(L) --> Returns rectangle FEDG coordinates
def FEDG(B,alpha,L):
    F = B[0] + L*m.cos(alpha) , B[1] + L*m.sin(alpha)
    E = B[0] + -L*m.cos(alpha) , B[1] + -L*m.sin(alpha)
    D = B[0] + -L*m.cos(alpha)+L*m.sin(alpha) , B[1] + -1*L*m.sin(alpha)-1*L*m.cos(alpha)
    G = B[0] + L*m.cos(alpha)+L*m.sin(alpha) , B[1] + L*m.sin(alpha) - L*m.cos(alpha)
    return F,E,D,G

