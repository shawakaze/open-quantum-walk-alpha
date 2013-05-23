from qutip import *
from HilbertSpace import *
from cmath import sqrt
from Kspace import Kspace

i = sqrt(-1)
H = Hadamardgate()
I = I()
I3 = qeye(2)
v0 = basis(2,0)
v1 = basis(2,1)
K=Kspace(9)

def R(G,t):
    return cos(t/2.)*I - i*sin(t/2)*G

def Bounds(A,G,t):
    U = Ugate(A,2)
    U = Qobj(U)
    B11 = tensor(I,I,I3)
    B12 = tensor(I,H,I3)
    B23 = tensor(I,v0*v0.dag(),I3)+ tensor(I,v1*v1.dag(),U)
    B34 = B12
    B45 = tensor(I,v0*v0.dag(),I3)+tensor(R(G,t),v1*v1.dag(),I3)
    B56 = B12
    B67 = B23.dag()
    B78 = B12
    B89 = tensor(v1*v1.dag(),I,I3)
    B99 = B11
    return [B11,B12,B23,B34,B45,B56,B67,B78,B89,B99]

def ForwardPropagation(A,G,t):
    L = []
    for i in range(1,10):
        L.append(Bounds(A,G,t)[i])
    return L

def ReversePropagation(A,G,t):   
    L = []
    for i in range(0,9):
        L.append(Bounds(A,G,t)[i])
    return L

def SupForward(w,A,G,t):
    L = []
    w = sqrt(w)
    fp = ForwardPropagation(A,G,t)
    for i in range(8):
        L.append(tensor(w*fp[i],K[i+1]*K[i].dag()))
    L.append(tensor(w*fp[8],K[8]*K[8].dag()))
    return L

def SupReverse(l,A,G,t):
    L = []
    l = sqrt(l)
    rp = ReversePropagation(A,G,t)
    L.append(tensor(l*rp[0],K[0]*K[0].dag()))
    for i in range(1,9):
        L.append(tensor(l*rp[i],K[i-1]*K[i].dag()))
    return L 

def PureForward(A,G,t):
    L = []
    fp = ForwardPropagation(A,G,t)
    for i in range(8):
        L.append(tensor(fp[i],K[i+1]*K[i].dag()))
    L.append(tensor(fp[len(fp)-1],K[8]*K[8].dag()))
    return L

def PureReverse(A,G,t):
    L = []
    rp = ReversePropagation(A,G,t)
    L.append(tensor(rp[0],K[0]*K[0].dag()))
    for i in range(1,9):
        L.append(tensor(rp[i],K[i-1]*K[i].dag()))
    return L 

def Projection(N,i):
    a = tensor(I,I,I3,Kspace(N)[i]*Kspace(N)[i].dag())
    return a
           