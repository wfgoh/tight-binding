from numpy import *
from readinput import lat,norb,orbitals,tbfilename

def convert(filename=tbfilename,norb=norb,orbitals=orbitals,lat=lat):
    '''
    type filename : str
    type tb : list[str]
    type norb : int
    type orbitals : list[str]
    type lat : array[float]
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

    # Create Orbitals Dictionary
    dict_orb = {}
    for i,orb in enumerate(orbitals):
       dict_orb[orb] = i

    # Read/write TB File
    f = open('tbwannier90format','w')
    for line in tb:
        if line != ' \n' and line != '\n':
            if line.split()[0] == 'spin':
                t=0
                i = dict_orb[line.split()[3].replace(')','')]
                j = dict_orb[line.split()[6].replace(')','')]
            elif line.split()[0] == 'T=':
                print('{:<10} {:<10} {:<10} {:<5} {:<5} {:<20} {:<20}'.format(line.split()[1], line.split()[2], line.split()[3], i+1, j+1, line.split()[5], line.split()[7]), file=f)
    
    f.close()
    print('CONVERT TO WANNIER90 FORMAT... DONE')
