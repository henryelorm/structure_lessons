from ase import Atoms
from ase.visualize import view
from ase.io import write
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton, GoodOldQuasiNewton

a = 2.0

n_molecule = Atoms(symbols='N2', positions=[[0, 0, 0], [0, 0, a]])


n_molecule.calc =  EMT()

# dyn = GoodOldQuasiNewton(n_molecule, trajectory='N2_molecule.traj')

# dyn.run(fmax=0.05)

e_mol = n_molecule.get_total_energy()

print(e_mol)

view(n_molecule)

write(filename='N2_molecule.traj', images=n_molecule)
