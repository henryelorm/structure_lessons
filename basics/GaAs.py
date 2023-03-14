from ase.spacegroup import crystal
from ase.visualize import view


a = 5.75

size = 2
    

ga_as = crystal(symbols=['Ga', 'As'],  basis=[(0, 0, 0), (1/4, 3/4, 3/4)],
                spacegroup=216, size=(size, size, size), cellpar=[a, a, a, 90, 90, 90],)


view(ga_as)