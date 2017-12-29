#Scott Dickson
#12/21/2017
#Framework to train the linear prediction model
#X - n by d
#Y - n by 1
#Theta - d by 1
#Error: ||X*Theta-Y||^2


import numpy as np

#Given data and parameters return the current prediction error
def error(X, Y, Theta):
    A = np.dot(X,Theta) - Y
    return np.dot(A,A)
    
#Given data and current parameters return the gradient vector of the error function
def gradient(X, Y, Theta):
    return 2*np.dot(X.T,(np.dot(X,Theta) - Y))
    
#Run gradient descent for up to t steps
def optimize(x, y, alpha=0.05, t = 1000):
    d = len(x[0])
    print("D = " + str(d))
    print("Alpha = " + str(alpha))
    param = np.zeros((d,1)) #Initialize the parameter vector
    steps = 0
    while(steps < t):
        param -= alpha*gradient(x,y,param)
        steps += 1
    return param

if __name__ == '__main__':
    theta = np.array([[1],[2],[3]])      
    x = np.array([[1,1,1],[0,0,2]])
    y = np.array([[6], [6]])
    print (optimize(x,y))