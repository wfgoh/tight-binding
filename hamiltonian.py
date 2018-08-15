from numpy import *
from tightbinding import get_tb
from readinput import lat,norb,orbitals,klist,tbfilename

HR, R = get_tb(tbfilename,norb,orbitals,lat)
phase = lambda k: exp(1j*2*pi*(R*k.reshape(3,1,1,1)).sum(axis=0))
Hk = lambda k: (HR*phase(k)).sum(axis=0)

def zero_off_diag(H):
   '''
   type Hk : array
   '''
   l = arange(int(H.shape[0]/2))
   for i in range(H.shape[0]):
      for j in range(H.shape[0]):
         if (i in l and j not in l) or (i not in l and j in l):
            H[i][j] = 0
   return H
