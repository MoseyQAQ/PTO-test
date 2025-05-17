# 1. set up calculator
from calc import calc

# 2. read structure
from ase.io import read
T = read('T_relaxed.vasp')
T.calc = calc

# 3. phonon calculation
from calorine.tools import get_force_constants
from phonopy.api_phonopy import Phonopy
from phonopy.phonon.band_structure import get_band_qpoints_and_path_connections

path = [
    [[0.0, 0.0, 0.0], # G
    [0.0, 0.5, 0.0], # X
    [0.5, 0.5, 0.0], # M
    [0.0, 0.0, 0.0], # G
    [0.0, 0.0, 0.5], # Z
    [0.0, 0.5, 0.5], # R
    [0.5, 0.5, 0.5], # A
    [0.0, 0.0, 0.5]]  # Z
]
labels = ['G', 'X', 'M', 'G', 'Z', 'R', 'A', 'Z']
phonon: Phonopy = get_force_constants(structure=T, calculator=calc, supercell_matrix=[2, 2, 2])
qpoints, connections = get_band_qpoints_and_path_connections(path, npoints=101)
phonon.run_band_structure(qpoints, path_connections=connections, labels=labels)
phonon.write_yaml_band_structure(filename='band.yaml')
phonon.plot_band_structure().savefig('phonon-ref.png', dpi=300)