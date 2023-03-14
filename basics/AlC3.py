from ase.spacegroup import crystal
from ase.visualize import view
from ase.io.vasp import read_vasp
from ase.atoms import Atom


a = 3.21

size = 1

# al_c =  read_vasp(file='AlC3.poscar')
al_c = crystal(symbols=['Al', 'C'],  basis=[(0, 0, 0), (0, 1/2, 1/2)],
                spacegroup=221, size=(size, size, size), cellpar=[a, a, a, 90, 90, 90],)


hyd = Atom(symbol='H', position=(0, a/2, (3/4)*a))

al_c.append(atom=hyd)





print(al_c.cell)

view(al_c)





