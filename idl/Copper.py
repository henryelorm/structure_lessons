from ase.build import bulk, diamond111
from ase.visualize import view


a = 5.4


struct = diamond111(symbol='Si', a=a, vacuum=6, size=(4, 4, 3))


view(struct)