from calc import calc
from ase.io import read 
from ase.md.npt import NPT
from ase.md.langevin import Langevin
from ase import units
import numpy as np
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

def md(atom, calc, timestep,temp,traj_name,log_name,nstep,loginterval=10):
    atom.set_calculator(calc)
    dyn = Langevin(
        atoms=atom,
        timestep=timestep*units.fs,
        temperature_K=temp,
        friction=0.01 / units.fs,
        trajectory=traj_name,
        logfile=log_name,
        loginterval=loginterval,
        append_trajectory=False
    )
    dyn.run(nstep)

if __name__ == "__main__":
    dt=2
    nstep=50000
    dstep=10

    for T in [300, 400, 500, 600, 700, 800, 900, 1000]:
        atom = read("../POSCAR")
        MaxwellBoltzmannDistribution(atom, temperature_K=T)
        traj_name = f"{T}K.traj"
        log_name = f"{T}K.log"
        md(atom, calc, dt, T, traj_name, log_name, nstep, dstep)
