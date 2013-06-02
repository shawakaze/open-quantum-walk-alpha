########## system modules ####################################
import numpy as np
from qutip import *
import pylab as pl
from time import time
########### my modules #######################################
from HilbertSpace import *
from Operators import *
from Kspace import *
from Detector import *
from solver import *
######### matplotlib module ##################################
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')
##############################################################

i = csr(-1)
K = Kspace(9)
P9 = Projection(9,8)
##############################################################
v0 = basis(2,0)
v1 = basis(2,1)
##############################################################
"""
    The A operator
"""
A = (1/csr(2))*matrix([[2,0],[0,-1]])

###########################################################
#  the b vector expressed in terms of the eigenvectors of A

b = (1/csr(2))*array([[1],[1]])

############################################################
## calculation of $\theta$ #####
theta = thetafn(A)

### real solution   #####################################
real_solution = DM(A,b)
###########################################################

################################################################
"""
    Inital density matrix
"""
g = Qobj(b)
g = g.unit()

p0 = tensor(v1*v1.dag(),v0*v0.dag(),g*g.dag(),K[0]*K[0].dag())


def main(w):
    l = 1-w
    exit_status = False
    P = [p0]

    #####################################################################
    Kf = SupForward(w,A,theta)
    Kb = SupReverse(l,A,theta)

    n = 0
    while not exit_status:
        Zero_ = tensor(Z(2),Z(2),Z(2),Z(9))
        for j in range(9):
            Zero_ = Zero_ + CPTPmap(Kf[j],Kb[j],P[n])

        P.append(Zero_)
        n = n + 1
        if n>10 :
            exit_status = True
        else:
            exit_status = False
        
    solution = P[len(P)-1]*P9
    return [ptrace(solution,2),solution]
    
##########################################################

def draw():
    x,y,z=[],[],[]
    delta = 0.01
    for w in arange(0,1,delta):
          p = main(w)
          solution = p[0]
          l = p[1]
          x.append(w)
          y.append(Probabilityfn(l))
          z.append(fidelity(solution,real_solution))

    pl.figure(1)
    pl.title(r"Probability of detection vs $\omega$")
    pl.ylabel(r"Probability of detection at node 9, $p_9$")
    pl.xlabel(r"$\omega$ - forward propagation amplitude")
    pl.xlim(0,1)
    pl.ylim(0,1.4)

    plot1, = pl.plot(x,y,'r')
    pl.legend([plot1],['Probability of detection at node 9'],'upper left')
    pl.savefig("App1.png")
#-------------------------------------------------------------------------------
    pl.figure(2)
    pl.title(r"Fidelity (actual,oqw) vs $\omega$")
    pl.ylabel(r"Fidelity,$\mathcal{F}(actual-dm,oqw-dm)$")
    pl.xlabel(r"$\omega$ - forward propagation amplitude")
    pl.xlim(0,1)
    pl.ylim(0,1.2)
    
    plot2, = pl.plot(x,z,'b')
    pl.legend([plot2],['fidelity between the two solns'],'upper left')
    pl.savefig("Apf1.png")

    pl.show()




#draw()
print main(0.5)

#print main(0.98),"\n\nWith theta as",theta
                  
