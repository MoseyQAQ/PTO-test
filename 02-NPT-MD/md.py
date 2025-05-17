from calc import calc
from ase.io import read 
from ase.md.npt import NPT
from ase import units
import numpy as np
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

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
    nstep=50000
    dstep=10

    for T in [300, 400, 500, 600, 700, 800, 900, 1000]:
        atom = read("POSCAR")
        MaxwellBoltzmannDistribution(atom, temperature_K=T)
        traj_name = f"{T}K.traj"
        log_name = f"{T}K.log"
        md(atom, calc, dt, T, traj_name, log_name, nstep, dstep)
