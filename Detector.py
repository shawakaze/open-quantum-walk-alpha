from qutip import *
from Kspace import *
from Operators import *

def CPTPmap(A,B,p):
    a = A*p*A.dag() + B*p*B.dag()
    return a

def NormalizationCondition(A,B):
    return A.dag()*A + B.dag()*B

def AntiCommutator(A,B):
    return A*B+B*A

def Probabilityfn(A):
    a = ptrace(A,[0,1,2])
    return a.tr()

def TraceDistance(A,B):
    a = A - B
    b = a.dag()*a
    b = b.sqrtm()
    return 0.5*b.tr()

def Expectation(M,p):
    c = (M*p).tr()
    return c
