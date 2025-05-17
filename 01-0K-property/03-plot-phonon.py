#!/usr/bin/python
import numpy as np
import matplotlib.pylab as plt
from math import sqrt
import matplotlib.cm as cm

fig, ax = plt.subplots(figsize=(4.0, 3.0))

data1 = np.loadtxt("phonon.dat", skiprows=2)

# 3915/261 = 15
Nband = 15
#nunmber of piecewise = Nkpt - 1
Npoint = 7
#points of every band
Nbandpts = 101 * Npoint
Nbandpts1 = 101 * Npoint

#ax.plot(data1[:, 0], data1[:, 1], 'k.', markersize=0.2, label='DP')
ax.plot(data1[0:Nbandpts, 0], data1[0:Nbandpts, 1], 'b-', linewidth=0.6, label='DP')


for i in range(1, Nband):
    ax.plot(data1[(i*Nbandpts):(i*Nbandpts+Nbandpts), 0], data1[(i*Nbandpts):(i*Nbandpts+Nbandpts), 1], 'b-', linewidth=0.5)
    
#i=0
#ax.plot(data2[0:357, 0], data2[0:357, 1], 'r-', linewidth=0.5, label='DFT')
Kpts = list(map(float, open('phonon.dat').readlines()[1].split()[1:]))
Kname = [r'$\Gamma$', r'$\rm{X}$', r'$\rm{M}$', r'$\Gamma$', r'$\rm{Z}$', r'$\rm{R}$', r'$\rm{A}$', r'$\rm{Z}$']
#plt.xlim(-0.2, 1.0)

for Kp in Kpts[1:-1]:
    print(Kp)
    plt.axvline(Kp, color='k', linewidth=0.6)

plt.axhline(0, color='k', linewidth=0.6)

plt.xticks(Kpts, Kname)

#ax.legend(loc='best', ncol=1)
#ax.set_ylim([emin, emax])
ax.set_xlim([0.0, Kpts[-1]])
#ax.set_xlabel(r'K_path')
ax.set_ylabel(r'Frequency (THz)')
fig.tight_layout(pad=0.2)
fig.savefig('phonon.png',bbox_inches='tight',dpi=300)
