#from __future__ import print_function
import numpy, pylab as pl

def plot1():
    x,y,z=[],[],[]
    numz = numpy.linspace(1,3)
    for i in numz:
        x.append(i)
        y.append(numpy.log(i))
        z.append(i**3)
    plotxy = pl.plot(x,y,'r')
    plotxz = pl.plot(x,z,'b')
    pl.show()

plot1()