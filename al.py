from ase.spacegroup import crystal
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton

a =  4.04


al = crystal(symbols='Al', basis=[ (0,0,0)], spacegroup=225, cellpar=[a, a, a, 90, 90, 90], size=(2,2,2))

# al.calc = EMT()

# dyn = QuasiNewton(al, trajectory='Al_crystal.traj')

# dyn.run()

print(al)

view(al)