#Scott Dickson
#1/15/2018
#FFT Implementation

import numpy as np
import cmath

def fft(samples):
    N = len(samples)
    
    
#Given vectors a and b return their convolution
def convolution(a,b):
    m = len(a)
    b = len(b)
    [k_sum(i) for i in range(m+n-1)]
     
#Given vectors a,b and target sum k return the sum of all a[i]b[j]
#Such that i+j=k and both are within range
def k_sum(a,b,k):
    s = 0
    m = len(a)
    n = len(b)
    for i in range(k):
        if i < m and (k - i) < n:
            s += a[i]*b[k-i]
            
#Return the DFT of the given input signal            
def dft(x):
    N = len(x)
    w = pow(cmath.e,-2*cmath.pi*(complex(0,1)/N))
    base_vec = np.array([w**i for i in range(N)])
    W_mat = [base_vec**i for i in range(N)]
    return np.dot(W_mat,x)

if __name__ == '__main__':
    x = [1,2,3]
    print(dft(x))
    
    