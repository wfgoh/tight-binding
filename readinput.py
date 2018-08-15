from numpy import *
# TB file
tbfilename = 'tb'
# lattice constant
lat = array([5.4, 5.4, 5.4])
# number of orbitals
norb = 18
# orbitals
orbitals = [
'4s+0up',
'4p-1up',
'4p+0up',
'4p+1up',
'3d-2up',
'3d-1up',
'3d+0up',
'3d+1up',
'3d+2up',
'4s+0dn',
'4p-1dn',
'4p+0dn',
'4p+1dn',
'3d-2dn',
'3d-1dn',
'3d+0dn',
'3d+1dn',
'3d+2dn',
]
# hligh symmetry points for band plot
klist = array([
[0, 0, 0],
[0, 1, 0],
[0.5, 0.5, 0],
[0, 0, 0],
[0.5, 0.5, 0.5],
[0, 1, 0]
])
