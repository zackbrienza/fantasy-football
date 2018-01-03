#Scott Dickson
#Feed forward neural network implementation
#1/1/2018
from math import exp 
import numpy as np

#Store weight vector for each layer
Thetas = np.array([])
width = 3
activation = np.vectorize(lambda x: 1/(1+exp(-x)) ) 

#Run an input through the trained network
def eval(x):
    res = x
    for w in Thetas:
        res = activation(np.dot(w,res))              
    return res[0]

#Initialize an array of the right size. Should start with dimension d as input
#and end with a dim 1 constant. Middle layers should be of dimention w
def init_network(d, layers):
    
    Thetas = [[]]*layers
    
    Thetas[0] = np.zeros((w,d))    
    
    for i in range(layers - 2):
        Thetas[i+1] = np.zeros((w,w))
       
    Thetas[layers - 1] = np.zeros((1,w)) if layers != 1 else np.zeros((1,d))
 
#Run an iteration of the backpropogation algorithm
def backpropogation():
    layers = len(Thetas)
    deltas = np.zeros(layers)
    #Implement from the hw6 documents 
    for i in reversed(range(layers)):
        pass
    
def optimize(X, Y, layers,alpha=0.05,t=1000):
    steps = 0
    init_network(layers)  
    
    
    
    
    

if __name__ == '__main__':
    print("Reached Main")