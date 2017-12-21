#Scott Dickson
#12/21/2017
#Framework to train the prediction model


#Data must be a matrix of size n by (d+1) and param must be a vector
#of size d
def error(data, param):
    s = 0
    d = len(data[0]) - 1
    for row in data:
        s += (dot(row[0:d],param) - row[d])**2 # Err += (a^T*x_i - y_i)^2
    return s

#Dot product of two arrays        
def dot(v1,v2):
    s = 0
    for i in range(len(v1)):
        s += v1[i]*v2[i]
    return s


if __name__ == '__main__':
    p = [1,2,3]        
    data = [[1,1,1,6],[0,0,2,6]]
    print(error(data,p))