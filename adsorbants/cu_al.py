from ase.visualize import view
from ase.atoms import Atom
from ase.io.vasp import read_vasp
from ase.build import fcc100, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton


a = 3.58

vac = 10
size_x = 5
size_y = 5
size_z = 2


# slab_1 = fcc100(symbol='Al', a=a, vacuum=vac,
#                       size=(size_x, size_y, size_z), periodic=True)


slab_1 = read_vasp('POSCAR')

atom = Atom(symbol='')


# slab_2 = fcc100(symbol='Au', a=a,
#                       size=(1, 1, 1), periodic=True)

# add_adsorbate(slab=slab_1, height=1.6,)

# slab_1.center(axis=0,)

# slab_1.calc = EMT()



# # Initial state:
# qn = QuasiNewton(slab_1, trajectory='initial.traj')
# qn.run(fmax=0.05)

# # Final state:
# slab_1[-1].x += slab_1.get_cell()[0, 0] / 2
# qn = QuasiNewton(slab_1, trajectory='final.traj')
# qn.run(fmax=0.001)


view(slab_1)