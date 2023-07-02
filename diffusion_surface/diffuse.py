from ase.io import read
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import LBFGS

from ase.visualize import view


init = read('initial.traj')
final = read('final.traj')


# images = [init]
# for image in range(5):
#     image = init.copy()
#     image.calc  = EMT()
#     images.append(image)

# images.append(final)


# neb = NEB(images)
# neb.interpolate()
# qn = LBFGS(neb, trajectory='neb.traj')
# qn.run(fmax=0.002)



#=---- checking results from neb.traj ---

data =  read('neb.traj@1029:')
print(len(data))
view(data)


