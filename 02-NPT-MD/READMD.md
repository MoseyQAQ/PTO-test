# 02-NPT-MD Folder Summary

This folder contains scripts and input files for running NPT (constant Number, Pressure, Temperature) molecular dynamics simulations of perovskite oxides. Below is a summary of each file:

- **calc.py**: Example code for setting up different machine learning interatomic potentials (UniPero, CHGNet, ORB, SevenNet, MACE, GPTFF, M3GNET) for use in calculations.
- **md.py**: Python script to perform NPT molecular dynamics using ASE. It sets up the simulation, applies the chosen calculator, and runs the MD trajectory.
- **POSCAR**: VASP-format input file describing the atomic structure (supercell) to be used in the MD simulation.

## How to Run This Test

1. Open a terminal in this directory (`02-NPT-MD`).
2. Run the MD simulation using the following command in PowerShell:

```powershell
python md.py
```

> **Note:**
> - Make sure all required Python packages (ASE, numpy, etc.) and model files are installed and available.
> - Edit `calc.py` to select and configure the desired machine learning potential before running the simulation.
> - The output trajectory and log files will be generated as specified in `md.py`.
