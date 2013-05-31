<<<<<<< HEAD
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

def Lindblad(A,B,p):
    a = A*p*A.dag()+B*p*B.dag() - 0.5*AntiCommutator(A*A.dag()+B*B.dag(),p)
    return a

def Detection(A,B,p):
    Zero_ = tensor(Z(2),Z(2),Z(2),Z(9))
    g = Zero_
    for j in range(9):
        g = g + Lindblad(A[j],B[j],p)
    return g

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

def PercError(exact,experimental):
    E = abs(exact-experimental)/exact
    E = E*100
    if 0<=E<=100:
        return E
    else:
        pass


=======
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

def Lindblad(A,B,p):
    a = A*p*A.dag()+B*p*B.dag() - 0.5*AntiCommutator(A*A.dag()+B*B.dag(),p)
    return a

def Detection(A,B,p):
    Zero_ = tensor(Z(2),Z(2),Z(2),Z(9))
    g = Zero_
    for j in range(9):
        g = g + Lindblad(A[j],B[j],p)
    return g

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

def PercError(exact,experimental):
    E = abs(exact-experimental)/exact
    E = E*100
    if 0<=E<=100:
        return E
    else:
        pass


>>>>>>> master/master
         