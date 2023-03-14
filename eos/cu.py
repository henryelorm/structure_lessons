
import numpy as np


from ase.visualize import view
from ase.spacegroup import crystal
from ase.calculators.emt import EMT
from ase.io.trajectory import Trajectory

from ase.io import read
from ase.units import kJ
from ase.eos import EquationOfState





a = 3.58
size = 2

step_size = 14
init_val  = 2.0
final_val = 4.0

cu = crystal(symbols='Cu',  basis=[(0, 0, 0)],
                spacegroup=221, size=(size, size, size), cellpar=[a, a, a, 90, 90, 90], pbc=True)


cu.calc = EMT()

traj = Trajectory(filename='cu.traj', mode='w')
cell = cu.get_cell()

for i  in np.linspace(init_val, final_val, step_size):
    print(f'########## {i} ##########################')
    cu.set_cell(cell * i, scale_atoms=True)
    energy = cu.get_potential_energy()

    print(energy)
    traj.write(cu)



## ploting the final the EOS
configs = read('cu.traj@0:5') 

volumes = [cu.get_volume() for cu in configs]
energies = [cu.get_potential_energy() for cu in configs]
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(B / kJ * 1.0e24, 'GPa')
eos.plot('Cu-eos.png')


# view structure
view(cu)


