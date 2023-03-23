from ase.io import read
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

from ase.visualize import view


init = read('initial.traj')
final = read('final.traj')


images = [init]
for im in range(6):
    image = init.copy()
    image.calc  = EMT()
    images.append(image)

images.append(final)


# neb = NEB(images)
# neb.interpolate()
# qn = BFGS(neb, trajectory='neb.traj')
# qn.run(fmax=0.05)

#=---- checking results from neb.traj ---

data =  read('neb.traj@3:')

view(data)


