# 0K property Test

> This folder contains scripts and input files for calculating 0 K properties of PbTiO$\mathrm{_3}$.

This folder contains scripts and input files for calculating 0 K properties of perovskite oxides. Below is a summary of each file:

- **00-perform-calc.sh**: Shell script to automate the workflow: removes old results, runs structure relaxation, phonon calculation, and phonon band structure plotting.
- **01-vc-relax.py**: Python script for variable-cell relaxation of the cubic and tetragonal structures using ASE and a machine learning potential defined in `calc.py`.
- **02-phonon.py**: Python script to perform phonon calculations on the relaxed tetragonal structure, using Phonopy and custom tools.
- **03-plot-phonon.py**: Python script to plot the phonon band structure from the calculated data.
- **calc.py**: Example code for setting up different machine learning interatomic potentials (UniPero, CHGNet, ORB, SevenNet, etc.) for use in calculations.
- **C.vasp**: VASP-format input file for the cubic phase structure of PbTiO$\mathrm{_3}$ (has been relaxed by DFT using PBEsol)
- **T.vasp**: VASP-format input file for the tetragonal phase structure of PbTiO$\mathrm{_3}$ (has been relaxed by DFT using PBEsol).
- **T_mp.vasp**: Alternative VASP-format input for the tetragonal phase of PbTiO$\mathrm{_3}$ (obatined from Materials Project, which has been relaxed using PBE).

## How to Run This Test

1. Modified the `calc.py` file to select the desired machine learning potential (e.g., UniPero, CHGNet, ORB, SevenNet).
2. Run the workflow using the following command:

```bash
bash 00-perform-calc.sh
```

> **Note:**
> - Make sure all required Python packages (ASE, Phonopy, etc.) and model files are installed and available.
