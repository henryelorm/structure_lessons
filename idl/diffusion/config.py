from ase.build import fcc100, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.visualize import view
from ase.optimize import QuasiNewton



slab = fcc100(symbol='Al', size=(3,3,4))

add_adsorbate(slab=slab, adsorbate='Au', height=1.8)

slab.center(axis=2, vacuum=4)

masks = []

for i in slab:
    constrain = i.tag > 2
    masks.append(constrain)
    
    

slab.set_constraint(FixAtoms(mask=masks))

slab.calc = EMT()

# initial configuration 
initial_opt = QuasiNewton(atoms=slab, trajectory='initial.traj')
initial_opt.run(fmax=0.005)
view(slab)

slab[-1].x += slab.get_cell()[0, 0]/2


# final configuration 
final_opt = QuasiNewton(atoms=slab, trajectory='final.traj')
final_opt.run(fmax=0.005)

view(slab)