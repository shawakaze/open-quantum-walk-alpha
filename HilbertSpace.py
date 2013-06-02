from qutip import *
from scipy.linalg import expm2
from cmath import sqrt
import numpy as np

i = sqrt(-1)

def Hadamardgate():
    return (1/sqrt(2))*Qobj(matrix([[1,1],[1,-1]]))
"""
    The next gate is not unitary
"""
def R(G,t):
    return cos(t/2.)*I - i*sin(t/2)*G

def Ugate(A,N):
     return Qobj(expm2(2*np.pi*i*N*A))

def I():
    return qeye(2)

def Z(n):
    a = np.zeros(n*n)
    a.shape = (n,n)
    a = np.matrix(a)
    return Qobj(a)
