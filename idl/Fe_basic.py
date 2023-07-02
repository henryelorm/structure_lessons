from ase.build import bulk
from ase.visualize import view


lattice_constant = 4.04


fe = bulk(name='Al', a=lattice_constant, crystalstructure='fcc')


view(fe)
