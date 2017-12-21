#Scott Dickson
#12/21/2017
#Framework to train the prediction model

#TODO: Vectorize this crap and actually use np

#Data must be a matrix of size n by (d+1) and param must be a vector
#of size d
def error(data, param):
    s = 0
    d = len(data[0]) - 1
    for row in data:
        s += (dot(row[0:d],param) - row[d])**2 # Err += (a^T*x_i - y_i)^2
    return s

#Given data and current parameters return the gradient vector of the error function
#Currently assuming a linear model
def gradient(data,param):
    d = len(param)
    g = d*[0] #Initialize
    
    for i in range(d):
        for row in data:
            print(len(param))
            print(len(row[0:d]))
            g[i] += 2*row[i]*(dot(param,row[0:d]) - row[d])**2
    return g
    
#Run gradient descent until some threshold is met
def optimize(data, alpha=0.5,t = 1):
    d = len(data[0]) - 1
    param = d*[0] #Initialize the parameter vector
    steps = 0
    #while(error(data,param) > delta):
    while(steps < t):
        param = add(param,mul(gradient(data,param),alpha)) #Update the vector
        steps += 1
    return param

#Dot product of two arrays        
def dot(v1,v2):
    s = 0
    for i in range(len(v1)):
        s += v1[i]*v2[i]
    return s

#Multiply vector by constant
def mul(v,c):
    for i in range(len(v)):
        v[i] = c*v[i]
    return v

#Add two equal sized vectors
def add(v1,v2):
    for i in range(len(v1)):
        v1[i] += v2[i]
    return v1



if __name__ == '__main__':
    p = [1,2,3]        
    data = [[1,1,1,6],[0,0,2,6]]
    print (optimize(data))