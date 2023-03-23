from ase.build import fcc100, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton


from ase.visualize import view


slab_al = fcc100(symbol='Al', size=(3,3,4), )

add_adsorbate(slab=slab_al, adsorbate='Au', height=1.8)

slab_al.center(axis=2, vacuum=4.0)


masks  = []
for i in slab_al:
    constrain = i.tag > 1
    masks.append(constrain)

slab_al.set_constraint(FixAtoms(mask=masks))


slab_al.calc = EMT()

#initial configuration
opt = QuasiNewton(atoms=slab_al, trajectory='initial.traj')
opt.run(fmax=0.05)


# Final configuration:
slab_al[-1].x += slab_al.get_cell()[0, 0] / 2
# slab_al[-1].y += slab_al.get_cell()[1, 1] / 2

opt = QuasiNewton(atoms=slab_al, trajectory='final.traj')
opt.run(fmax=0.05)


view(slab_al)


