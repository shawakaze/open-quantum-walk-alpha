<<<<<<< HEAD
import numpy as np
from qutip import *
from HilbertSpace import *
from Operators import *
from Kspace import *

K = Kspace(9)
Y = Ygate()
w = 0.8
l = 1 - w
pi = np.pi

##############################################################
v0 = basis(2,0)
v1 = basis(2,1)
b = v1
# density matrix     ############################
p0 = tensor(v1*v1.dag(),v0*v0.dag(),b*b.dag())
p0 = tensor(p0,K[0]*K[0].dag())
P = [p0]


############ M operators ##################################################
Kf = SupForward(w,Y,pi/2.)
Kb = SupReverse(w,Y,pi/2.)

exit_status = False

for j in range(9):
    g = Kf[j]*P[j]*Kf[j].dag() + Kb[j]*P[j]*Kb[j].dag()
    P.append(g)


solution = P[len(P)-1]
print solution

=======
import numpy as np
from qutip import *
from HilbertSpace import *
from Operators import *
from Kspace import *

K = Kspace(9)
Y = Ygate()
w = 0.8
l = 1 - w
pi = np.pi

##############################################################
v0 = basis(2,0)
v1 = basis(2,1)
b = v1
# density matrix     ############################
p0 = tensor(v1*v1.dag(),v0*v0.dag(),b*b.dag())
p0 = tensor(p0,K[0]*K[0].dag())
P = [p0]


############ M operators ##################################################
Kf = SupForward(w,Y,pi/2.)
Kb = SupReverse(w,Y,pi/2.)

exit_status = False

for j in range(9):
    g = Kf[j]*P[j]*Kf[j].dag() + Kb[j]*P[j]*Kb[j].dag()
    P.append(g)


solution = P[len(P)-1]
print solution

>>>>>>> master/master
