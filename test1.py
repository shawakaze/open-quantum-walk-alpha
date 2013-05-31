<<<<<<< HEAD
#from __future__ import print_function
from solver import *
from scipy import matrix
from qutip import * 
from HilbertSpace import *
from Kspace import *
from Operators import *
from Detector import *
from cmath import *
from numpy import *
import pylab as pl
from scipy.linalg import *
from time import time
from scipy import log
from numpy import arange

"""
use this file to test created modules
"""
=======
#from __future__ import print_function
from solver import *
from scipy import matrix
from qutip import * 
from HilbertSpace import *
from Kspace import *
from Operators import *
from Detector import *
from cmath import *
from numpy import *
import pylab as pl
from scipy.linalg import *
from time import time
from scipy import log
from numpy import arange

def plot1():
    x,y,z=[],[],[]
    for i in arange(1,3,0.01):
        x.append(i)
        y.append(log(i))
        z.append(i**3)

    plot1 = pl.plot(x,y,'r')
    plot2 = pl.plot(x,z,'b')
    pl.show()

plot1()
>>>>>>> master/master
