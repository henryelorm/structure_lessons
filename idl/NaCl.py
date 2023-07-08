from ase.spacegroup import crystal
from ase.visualize import view
from ase.io.vasp import read_vasp


a = 5.63
b = 8.00
c = 8.42

size=2



#struct = crystal(symbols=['Na', 'Cl'], basis=[(0, 0, 0), (0, 0, 1/2)],
#                 spacegroup=225, size=(size, size, size), 
#                 cellpar=[a, a, a, 90, 90, 90])


struct2 = crystal(symbols=['Na', 'Cl', 'Cl', 'Cl'],
    basis=[(1/4,	0.051,	0.821), (1/4, 0.358,	0.642), (1/4, 0.788, 0.581),(1/4,0.551, 0.88)],
    spacegroup=62, size=(size, size, size),cellpar=[a, b, c, 90, 90, 90] )

struct3 = read_vasp('NaCl3.poscar')

view(struct3)