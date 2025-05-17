rm vc-relax.log phonon.dat band.yaml # remove old files

python3 01-vc-relax.py
python3 02-phonon.py
phonopy-bandplot --gnuplot >> phonon.dat
python3 03-plot-phonon.py