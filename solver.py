from scipy.linalg import * 
from scipy import matrix,transpose,array
from qutip import *
import cmath
import scipy as sp


pi = sp.pi
def csr(a):
    return cmath.sqrt(a)
###############################################
def dec(a,b):
    if 0 <= abs(a)/abs(b) <=1:
        return a/b
    elif 0 <= abs(b)/abs(a) <= 1:
        return b/a
    else:
        return 0
##########################################
def thetafn(A):
    B = Qobj(A)
    b0 = min(B.eigenenergies())
    b1 = max(B.eigenenergies())
    return -2*sp.arccos(dec(b0,b1))
################################################
def DM(A,b): 
    b = b/norm(b)
    des = solve(A,b)
    des = Qobj(des)
    des = des.unit()
    return des*des.dag()
##########################################################
def EigenVectors(A):
    data = eig(A)
    g0 = data[1][0]
    g1 = data[1][1]
    g0.shape = (2,1)
    g1.shape = (2,1)
    g0 = matrix(g0)
    g1 = matrix(g1)
    return g0,g1

