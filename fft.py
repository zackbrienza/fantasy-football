#Scott Dickson
#1/15/2018
#FFT Implementation

import numpy as np
import cmath

def fft(samples):
    N = len(samples)
    return eval_roots(samples, [1]*n)
    
def fast_conv(a,b):
    pass

#Given a vector of coefficients for two polynomials a and b return another vector of
#the polynomial evaluated on the roots of unity for C(X) = A(X)B(X)
#assumption for now: len(A)=len(B)
def eval_roots(a,b):
    n = len(a)
    roots = np.array([pow(cmath.e,-2*cmath.pi*complex(0,1)/(2*n)) for i in range(2*n)])
    res = np.zeros((2*n))
    if n == 1:
        print("Reached base case")
        print(a)
        print(b)
        return [a[0]*b[0], a[0]*b[0]]
    even = eval_roots([a[2*i] for i in range((n+1)//2)],[b[2*i] for i in range((n+1)//2)])
    odd = eval_roots([a[2*i + 1] for i in range(n//2)],[b[2*i + 1] for i in range(n//2)])
    print(even)
    print(odd)
    #print("N is: " + str(n))    
    #As the 2nth roots of unity squared are the nth roots of unity
    #After the nth the (n/2) part cancels out and we get that res[i+n] = res[i]
    
    for i in range(2*n):
        res[i] = even[i % n] + roots[i % n]*odd[i % n]
    return res    
    
#Given n+1 values that a polynomial of dgree n takes on
#Return the n+1 coefficiants of the polynomial
def interpolate(values):
    pass
  

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
    a = [1,0,1,0]
    b = [1,0,0,0]
    print(eval_roots(a,b))
    
    