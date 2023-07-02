from ase.io import read
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.visualize import view


image_val = 6


data =  read(f'neb.traj@{1029 + image_val}')

data.calc =  EMT()

# BFGS(data).run(fmax=0.002)
vib = Vibrations(data, name=f'vib_{image_val}' )

vib.run()

summary = vib.summary(log=f'summary{image_val}.dat')




view(data)