#Scott Dickson
#12/21/2017
#Framework to train various prediction models
#dim(X):  n by d
#dim(Y): n by 1
#dim(Theta): d by 1
#Error: ||X*Theta-Y||^2

import numpy as np

#Given data and parameters return the current prediction error
def linear_error(X, Y, Theta):
    A = np.dot(X,Theta) - Y
    return np.dot(A,A)

#Here theta must be of size 2d
def quadratic_error(X,Y,Theta):
    d = len(X[0])
    A = np.dot(X,Theta[0:d]) + np.dot(X**2,Theta[d:]) - Y
    return np.dot(A.T,A)


def polynomial_error(X,Y, Theta):
    d = len(X[0])
    n = len(Theta) / d
    A =  (-1)*Y #Initialize sum
   
    for i in range(n):
        A += np.dot(X**(i+1),Theta[i*d:(i+1)*d])
    return A
   
#Given data and current parameters return the gradient vector of the error function
def linear_gradient(X, Y, Theta):
    return 2*np.dot(X.T,np.dot(X,Theta) - Y)

#Gradient of a model in the form of f(X,Theta) = x * Theta + x^2 * Theta
def quadratic_gradient(X, Y, Theta):
    d = len(X[0])
    X2 = X**2
        
    p1 = 2*np.dot(X.T, np.dot(X,Theta[0:d]) + np.dot(X2,Theta[d:]) - Y)
    p2 = 2*np.dot(X2.T, np.dot(X,Theta[0:d]) + np.dot(X2,Theta[d:]) - Y)
  
    return np.concatenate([p1,p2])
 
#Same as above but for general polynomial functions
def polynomial_gradient(X,Y,Theta):
    d = len(X[0])
    n = len(Theta) / d
    grad = np.array([])
    
    #Figure out the base part of the gradient
    base_grad = (-1)*Y
    
    for i in range(n):
        base_grad += np.dot(X**(i+1), Theta[d*i:d*(i+1)])
    
    #Figure out each section of the gradient vector    
    for j in range(n):
        grad.concatenate(grad,2*np.dot(X**(i+1).T, base_grad))
    
    return grad 
       
#Run gradient descent for up to t steps
def optimize(x, y, alpha=0.05, t=1000):
    d = len(x[0])
    param = np.zeros((d,1)) #Initialize the parameter vector
    steps = 0
    while(steps < t):
        param -= alpha*linear_gradient(x,y,param)
        steps += 1
    return param

#Also run gradient descent for up to t steps
def quad_optimize(x,y,alpha=0.005, t=1000):
    d = len(x[0])
    param = np.zeros((2*d,1))
    steps = 0
    
    while(steps < t):
        param -= alpha*quadratic_gradient(x,y,param)
        steps += 1
    print("Training Error: " + str(quadratic_error(x,y,param)[0][0]))    
    return param

#Again, gradient descent for up to t steps but this time fit
#a polynomial model of maximum degree [deg]
def polynomial_optimize(x,y,deg=2,alpha=0.005, t=1000):
    d = len(x[0])
    param = np.zeros((deg*d,1))
    steps = 0
    
    while(steps < t):
        param -= alpha*polynomial_gradient(x,y,param)
        steps += 1
    print("Training Error: " + str(polynomial_error(x,y,param)))
    return pararm 

if __name__ == '__main__':
    theta = np.array([[1],[2],[3]])      
    x = np.array([[1,1,1],[0,0,2]])
    y = np.array([[6], [6]])
    print (quad_optimize(x,y))