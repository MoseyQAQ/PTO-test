# 1. set up calculator
from calc import calc

# 2. read structure
from ase.io import read, write
C = read('C.vasp')
T = read('T.vasp')
C.calc = calc
T.calc = calc

# 3. set up optimization
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

ecf_c = FrechetCellFilter(C)
dyn_c = BFGS(ecf_c)
dyn_c.run(fmax=1e-3)
write('C.vasp', C)
print(f"C {' '.join(map(str, C.cell.cellpar()))} {C.get_potential_energy()}")

ecf_t = FrechetCellFilter(T)
dyn_t = BFGS(ecf_t)
dyn_t.run(fmax=1e-3)
write('T.vasp', T)
print(f"T {' '.join(map(str, T.cell.cellpar()))} {T.get_potential_energy()}")
