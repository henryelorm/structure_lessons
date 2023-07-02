from ase.spacegroup import crystal
from ase.visualize import view
from ase.io import read


# Mo bulk

a = 3.16

# mo = crystal(symbols='Mo', basis=[(0, 0, 0)], spacegroup=229, cellpar=[a, a, a, 90, 90, 90], size=(2, 2, 2))
fe = read('FeHO22.vasp')


view(fe)