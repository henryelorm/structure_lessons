from ase.io.vasp import read_vasp
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.optimize import BFGSLineSearch


struct =  read_vasp(file='POSCAR')


struct.calc = EMT()

dyn = BFGSLineSearch(atoms=struct, trajectory='Al_crystal.traj')

dyn.run(fmax=0.001)

print(struct.get_potential_energy())

view(struct)

