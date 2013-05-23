from scipy.linalg import * 
from scipy import matrix,transpose,array
from qutip import *
import cmath
import scipy as sp


pi = sp.pi
def csr(a):
    return cmath.sqrt(a)

def thetafn(A):
    B = Qobj(A)
    b0 = min(B.eigenenergies())
    b1 = max(B.eigenenergies())
    if b0 != 0 and b1 != 0:
        if abs(b0) < abs(b1):
            return -2*sp.arccos(b0/b1)
        else:
            return -2*sp.arccos(b1/b0)
    else:
        return 2*pi

def DM(A,b): 
    b = b/norm(b)
    des = solve(A,b)
    des = Qobj(des)
    des = des.unit()
    return des*des.dag()


def EigenVectors(A):
    data = eig(A)
    g0 = data[1][0]
    g1 = data[1][1]
    g0.shape = (2,1)
    g1.shape = (2,1)
    g0 = matrix(g0)
    g1 = matrix(g1)
    return g0,g1



