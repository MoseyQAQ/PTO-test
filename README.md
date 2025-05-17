# PTO-test Project Overview

This project contains scripts, input files, and models for first-principles and machine learning-based calculations on perovskite oxide materials (e.g., PTO). The structure is organized as follows:

- **01-0K-property/**: Scripts for 0 K property calculations, including structure relaxation, phonon calculations, and plotting. Contains VASP input files and example scripts for using different machine learning potentials (e.g., UniPero, CHGNet, ORB, SevenNet).
- **02-NPT-MD/**, **03-NVT-MD/**, **04-efficiency/**: Scripts and input files for molecular dynamics simulations under different ensembles and for efficiency testing.
- **models/**: Pre-trained machine learning potential files used in this test (e.g., CHGNet, UniPero, GPT-FF, MACE).