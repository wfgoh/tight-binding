from numpy import *

def get_tb(filename,norb,orbitals,lat):
    '''
    type filename : str
    type tb : list[str]
    type norb : int
    type orbitals : list[str]
    type lat : array[float]
    return :
    type HR : array[complex]
    type R : array[float]
    '''
    # Read File
    tbfile = open(str(filename),'r')
    tb = tbfile.readlines()
    tbfile.close()

    # Get Largest Hopping For Matrix Size
    i = 0
    hop = []
    for l in tb:
       i += 1
       if l != ' \n' and l != '\n':
           if l.split()[0] == 'spin':
               hop.append(i-1)
               i = 0
    maxhop = max(hop)

    # Create Empty Matrix
    HR = zeros((maxhop, norb, norb), dtype=complex)
    Rx = zeros((maxhop, norb, norb))
    Ry = zeros((maxhop, norb, norb))
    Rz = zeros((maxhop, norb, norb))

    # Create Orbitals Dictionary
    dict_orb = {}
    for i,orb in enumerate(orbitals):
       dict_orb[orb] = i

    # Read TB File
    for line in tb:
        if line != ' \n' and line != '\n':
            if line.split()[0] == 'spin':
                t=0
                i = dict_orb[line.split()[3].replace(')','')]
                j = dict_orb[line.split()[6].replace(')','')]
            elif line.split()[0] == 'T=':
                Rx[t,i,j] = line.split()[1]
                Ry[t,i,j] = line.split()[2]
                Rz[t,i,j] = line.split()[3]
                HR[t,i,j] = float(line.split()[5]) + 1j*float(line.split()[7])
                t+=1

    R = array([Rx,Ry,Rz])/lat.reshape(3,1,1,1)

    print('GET TIGHT BINDING... DONE')
    return HR, R
