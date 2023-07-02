from ase.spacegroup import crystal
from ase.visualize import view
from ase.io.vasp import write_vasp
from ase.io.lammpsdata import write_lammps_data


a = 4.04


al = crystal(symbols='Al', basis=[(0,0,0)], spacegroup=225, 
             cellpar=[a, a, a, 90, 90, 90], size=(1, 1, 1))


view(al)

write_vasp(file='POSCAR', atoms=al, direct=True)

#write_lammps_data(file='lammps_out',atoms=al )

