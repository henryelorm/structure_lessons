from ase.spacegroup import crystal
from ase.visualize import view
from ase.io import read


a, b, c = 2.91, 5.15, 5.17

angle = 90

basis = [(0,	0,	0), (0,	0,	1/2)]


struct = crystal(symbols=['As', 'Ga'], basis=basis, spacegroup=119, size=(1, 3, 3), 
                 cellpar=[a, b, c, angle, angle, angle])


view(struct)

