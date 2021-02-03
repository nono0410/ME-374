# Graphical simulation for extra credit 1

import math as m
import numpy as np
from scipy.optimize import fsolve
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import closer
import rect
plt.style.use('seaborn-pastel')

# Variable definitions
R = 2
L = 5
const = 4
O3x,O3y = 6,0
ref = -1

# Beta,theta angle definition
def eq(beta,theta):
    return ((-1*L*m.cos(beta) + O3x -R*m.cos(theta))**2 + (-1*R*m.sin(theta)+L*m.sin(beta) + O3y)**2)**0.5 - const

# Given angle(i) and previous angle(ref) --> Returns cooresponding B,C,and beta
def BC(i,ref):

    theta = m.radians(i)

    b__inti = fsolve(eq,ref,theta) # Initialize a rough solution
    beta = (b__inti[0])

    for n in range(360): # Finds closer beta
        test = fsolve(eq,m.radians(n),theta) # Result in radians
        beta = closer.closer(ref,beta,test[0])
        #print(m.degrees(ref),m.degrees(beta),m.degrees(test))
        
    B = R*m.cos(theta) , R*m.sin(theta)
    C = -1*L*m.cos(beta) + O3x , L*m.sin(beta) + O3y
    length = ((-1*L*m.cos(beta) + O3x -R*m.cos(theta))**2 + (-1*R*m.sin(theta)+L*m.sin(beta) + O3y)**2)**0.5
    #print(m.degrees(theta),m.degrees(beta),m.degrees(ref))

    return B,C,beta # Return B,C, and beta (radians)

# Plot and animate results with matplotlib
fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax.plot([], [], lw=3)
line1, = ax.plot([], [], lw=3)
line2, = ax.plot([], [], lw=3)
lineEF, = ax.plot([], [], lw=3)
lineED, = ax.plot([], [], lw=3)
lineDG, = ax.plot([], [], lw=3)
lineFG, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    lineEF.set_data([], [])
    lineED.set_data([], [])
    lineDG.set_data([], [])
    lineFG.set_data([], [])
    return line,line1,line2,lineEF,lineED,lineDG,lineFG

def animate(i):
    global ref
    B,C,ref = BC(i,ref) #i in range of 0 to 360
    alpha = m.atan((B[0]-C[0])/(C[1]-B[1]))
    F,E,D,G = rect.FEDG(B,alpha,const) # Get rectangle
    print(m.degrees(alpha))

    line.set_data([0,B[0]],[0,B[1]])
    line1.set_data([O3x,C[0]],[O3y,C[1]])
    line2.set_data([B[0],C[0]],[B[1],C[1]]) # BC link
    lineEF.set_data([E[0],F[0]],[E[1],F[1]])
    lineED.set_data([E[0],D[0]],[E[1],D[1]])
    lineDG.set_data([D[0],G[0]],[D[1],G[1]])
    lineFG.set_data([F[0],G[0]],[F[1],G[1]])
    return line,line1,lineEF,lineED,lineDG,lineFG #line2 BC link

anim = FuncAnimation(fig, animate, init_func=init,frames=360, interval=1, blit=True)
plt.show()
