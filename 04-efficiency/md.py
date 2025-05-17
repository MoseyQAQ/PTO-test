from calc import calc
from ase.io import read 
from ase.md.npt import NPT
from ase import units
import numpy as np
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from time import time
def upper_triangular_cell(atoms) -> None:
    atom = atoms.copy()
    if not NPT._isuppertriangular(atom.get_cell()):
        a, b, c, alpha, beta, gamma = atom.cell.cellpar()
        angles = np.radians((alpha, beta, gamma))
        sin_a, sin_b, _sin_g = np.sin(angles)
        cos_a, cos_b, cos_g = np.cos(angles)
        cos_p = (cos_g - cos_a * cos_b) / (sin_a * sin_b)
        cos_p = np.clip(cos_p, -1, 1)
        sin_p = (1 - cos_p**2) ** 0.5

        new_basis = [
                (a * sin_b * sin_p, a * sin_b * cos_p, a * cos_b),
                (0, b * sin_a, b * cos_a),
                (0, 0, c),
            ]

        atom.set_cell(new_basis, scale_atoms=True)
    return atom

def md(atom, calc, timestep,temp,traj_name,log_name,nstep,loginterval=10):
    mask = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    external_stress = 0.0
    atom = upper_triangular_cell(atom)
    atom.set_calculator(calc)
    dyn = NPT(
        atom,
        timestep=timestep*units.fs,
        temperature_K=temp,
        externalstress=external_stress,
        ttime=25 * units.fs,
        pfactor=75.0**2.0 * units.fs,
        trajectory=traj_name,
        logfile=log_name,
        loginterval=loginterval,
        mask=mask,
        append_trajectory=False,
    )
    dyn.run(nstep)

if __name__ == "__main__":
    dt=2
    nstep=500
    dstep=10
    Tlist = [300, 500, 700]
    Slist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with open("output.log", "a") as f:
        for S in Slist:
            for T in Tlist:
                atom = read("../POSCAR")
                atom *= (S, S, S)
                MaxwellBoltzmannDistribution(atom, temperature_K=T)
                traj_name = f"{S}-{T}.traj"
                log_name = f"{S}-{T}.log"
                start_time = time()
                md(atom, calc, dt, T, traj_name, log_name, nstep, dstep)
                end_time = time()
                
                output = f"Size: {S}, Temp: {T}, Time: {end_time - start_time} s\n"
                f.write(output)
                f.flush()
