from numpy import *
from matplotlib import pyplot as plt
from readinput import klist
from hamiltonian import Hk, zero_off_diag

def generate_full_kpoints(klist,binsize=20):
    kfull = [array(klist[0])]
    for i in range(len(klist)-1):
        delta = (array(klist[i+1])-array(klist[i]))/binsize
        [kfull.append(klist[i]+delta*(n+1)) for n in range(binsize)]
    return kfull

def plotband():
    band = empty(0)
    #band2 = empty(0)
    kfull = generate_full_kpoints(klist,30)
    for k in kfull:
        eig, eiv = linalg.eigh(Hk(k))
        #eig2, eiv2 = linalg.eigh(zero_off_diag(Hk(k)))
        band = append(band,eig)
        #band2 = append(band2,eig2)
    bandplot = band.reshape(-1,eig.size)
    #bandplot2 = band2.reshape(-1,eig2.size)
    i = 0
    f = open('band','w')
    for kp in bandplot:
        for ene in kp:
            print(i, ene,file=f)
            i += 1
    f.close()
    print('OUTPUT BAND STRUCTURE TO BAND... DONE')
    plt.plot(bandplot,'r+')
    #plt.plot(bandplot2,'b+')
    plt.ylim(-10,10)
    plt.show()
    print('PLOTTING BAND STRUCTURE... DONE')
    return
