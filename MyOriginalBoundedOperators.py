<<<<<<< HEAD
import qutip,numpy as np,random,pylab as pl
from Kspace import *

"""
    (0) N is the number of vertices on \mathbb{Z}
    (1) First we build a K-space basis states  ; K = C^V
    (2) Then the bounded operators.
    (3) Perform a simple iteration.

"""
# the number of vertices
N = 15

# (2) The Local bounded operators a walk on Z
def B_ops(N,j,i):
    b = (1./np.sqrt(3))*qutip.Qobj(np.matrix([[1,1],[0,1]]))
    c = (1./np.sqrt(3))*qutip.Qobj(np.matrix([[1,0],[-1,1]]))
    if i==j+1: return c
    if i==j-1: return b
    if i==j and j == 0: return b
    if i==j and j == N-1: return c

"""
    Normalization condition for the B operators
"""
def Bcomplete(N):
    p = []
    r = random.randint(0,N-1)
    for i in range(N):
        if i==r+1 or i==r-1:
            p.append(B_ops(N,r,i).dag()*B_ops(N,r,i))
    return sum(p)


# (3) The M state space operators
def M_ops(N,j,i):
    k = Kspace(N)
    op = k[i]*k[j].dag()
    if i==j+1 or i==j-1:
        return qutip.tensor(B_ops(N,j,i),op)
    if i==j and (j==0 or j==N-1):
        return qutip.tensor(B_ops(N,j,i),op)


"""
    Normaization condition
""" 
def Mcomplete(N):
    p = []
    for i in range(N):
        for j in range(N):
            if i==j+1 or i==j-1:
                p.append(M_ops(N,j,i).dag()*M_ops(N,j,i))
            if i==j and (j==0 or j==N-1):
                p.append(M_ops(N,j,i).dag()*M_ops(N,j,i))
    return sum(p)

"""
    We define the projection operator as follows
"""
def Projection(N,i):
    a = Kspace(N)[i]*Kspace(N)[i].dag()
    return a

# an arbitrary positive trace-class operator \rho
psi0 = Kspace(N)[0]
p0 = np.matrix([[1,0],[0,0]])
p0 = qutip.Qobj(p0)
p = qutip.tensor(p0,psi0*psi0.dag())

l = [p]

def SingleIteration(i):
    s=M_ops(N,N-1,N-2)*l[i-1]*M_ops(N,N-1,N-2).dag() + M_ops(N,0,0)*l[i-1]*M_ops(N,0,0).dag() + M_ops(N,0,1)*l[i-1]*M_ops(N,0,1).dag()
    for j in range(1,N-1):
        s+=M_ops(N,j,j+1)*l[i-1]*M_ops(N,j,j+1).dag() + M_ops(N,j,j-1)*l[i-1]*M_ops(N,j,j-1).dag()
    return s

def MultipleIterations(N,n): # n represents number of iterations to be considered
    for i in range(1,n):
        a = SingleIteration(i)
        l.append(a)
    return l

"""
 probability function reads as follows

 Probability(Number of vertices, iterations made, iteration matrix, node number)

"""    
def Prb(N,iterations,Itermatrix,site):  
    return (MultipleIterations(N,iterations)[Itermatrix].ptrace(1)*Projection(N,site)).tr()

n = 6
Iterations = n + 1   
Itermatrix = n


"""
    Graphical Illustration of open quantum walk probability distribution
"""

def draw():
    x,y=[],[]
    for i in range(N):
        x.append(i)
        y.append(Prb(N,Iterations,Itermatrix,i))
    pl.title("Homogenous open quantum walk on Z with some iterartions.")
    pl.ylabel("Probability")
    pl.xlabel("vertex number")
    pl.grid()
    pl.plot(x,y,'*')
    pl.show()
    print sum(y)

draw()
print Prb(N,Iterations,Itermatrix,4)
=======
import qutip,numpy as np,random,pylab as pl
from Kspace import *

"""
    (0) N is the number of vertices on \mathbb{Z}
    (1) First we build a K-space basis states  ; K = C^V
    (2) Then the bounded operators.
    (3) Perform a simple iteration.

"""
# the number of vertices
N = 15

# (2) The Local bounded operators a walk on Z
def B_ops(N,j,i):
    b = (1./np.sqrt(3))*qutip.Qobj(np.matrix([[1,1],[0,1]]))
    c = (1./np.sqrt(3))*qutip.Qobj(np.matrix([[1,0],[-1,1]]))
    if i==j+1: return c
    if i==j-1: return b
    if i==j and j == 0: return b
    if i==j and j == N-1: return c

"""
    Normalization condition for the B operators
"""
def Bcomplete(N):
    p = []
    r = random.randint(0,N-1)
    for i in range(N):
        if i==r+1 or i==r-1:
            p.append(B_ops(N,r,i).dag()*B_ops(N,r,i))
    return sum(p)


# (3) The M state space operators
def M_ops(N,j,i):
    k = Kspace(N)
    op = k[i]*k[j].dag()
    if i==j+1 or i==j-1:
        return qutip.tensor(B_ops(N,j,i),op)
    if i==j and (j==0 or j==N-1):
        return qutip.tensor(B_ops(N,j,i),op)


"""
    Normaization condition
""" 
def Mcomplete(N):
    p = []
    for i in range(N):
        for j in range(N):
            if i==j+1 or i==j-1:
                p.append(M_ops(N,j,i).dag()*M_ops(N,j,i))
            if i==j and (j==0 or j==N-1):
                p.append(M_ops(N,j,i).dag()*M_ops(N,j,i))
    return sum(p)

"""
    We define the projection operator as follows
"""
def Projection(N,i):
    a = Kspace(N)[i]*Kspace(N)[i].dag()
    return a

# an arbitrary positive trace-class operator \rho
psi0 = Kspace(N)[0]
p0 = np.matrix([[1,0],[0,0]])
p0 = qutip.Qobj(p0)
p = qutip.tensor(p0,psi0*psi0.dag())

l = [p]

def SingleIteration(i):
    s=M_ops(N,N-1,N-2)*l[i-1]*M_ops(N,N-1,N-2).dag() + M_ops(N,0,0)*l[i-1]*M_ops(N,0,0).dag() + M_ops(N,0,1)*l[i-1]*M_ops(N,0,1).dag()
    for j in range(1,N-1):
        s+=M_ops(N,j,j+1)*l[i-1]*M_ops(N,j,j+1).dag() + M_ops(N,j,j-1)*l[i-1]*M_ops(N,j,j-1).dag()
    return s

def MultipleIterations(N,n): # n represents number of iterations to be considered
    for i in range(1,n):
        a = SingleIteration(i)
        l.append(a)
    return l

"""
 probability function reads as follows

 Probability(Number of vertices, iterations made, iteration matrix, node number)

"""    
def Prb(N,iterations,Itermatrix,site):  
    return (MultipleIterations(N,iterations)[Itermatrix].ptrace(1)*Projection(N,site)).tr()

n = 6
Iterations = n + 1   
Itermatrix = n


"""
    Graphical Illustration of open quantum walk probability distribution
"""

def draw():
    x,y=[],[]
    for i in range(N):
        x.append(i)
        y.append(Prb(N,Iterations,Itermatrix,i))
    pl.title("Homogenous open quantum walk on Z with some iterartions.")
    pl.ylabel("Probability")
    pl.xlabel("vertex number")
    pl.grid()
    pl.plot(x,y,'*')
    pl.show()
    print sum(y)

draw()
print Prb(N,Iterations,Itermatrix,4)
>>>>>>> master/master
