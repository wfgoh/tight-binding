from numpy import *
from bandplot import plotband
#from hamiltonian import Hk, zero_off_diag
#from convertformat import convert

if __name__ == '__main__':
    plotband()
    
    #k = array([0,1,0]) # unit = 2pi/a
    #print(zero_off_diag((Hk(k))))
    #f = open('hout','w')
    #print(round_(zero_off_diag(Hk(k)),5),file=f)
    #f.close()
    #convert()
