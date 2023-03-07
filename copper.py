from ase.build import bulk, bcc111
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.io import write
from ase.optimize import QuasiNewton

a = 3.6

# simple primitive structure
a1 = bulk(name='Cu', crystalstructure='fcc', a=a, )


# surfaces
s1 = bcc111(symbol='Cu', size=(4, 4, 4), a=a, vacuum=12)

# attach a calculator 
s1.calc = EMT()

# calculate system energy
e_S1 =  s1.get_potential_energy()
print(e_S1)


# relax system
dyn = QuasiNewton(s1, trajectory='s1.traj')

dyn.run(fmax=0.001)


# view structure
view(s1)

# write/save as a cif file
write('cu.cif', s1)
