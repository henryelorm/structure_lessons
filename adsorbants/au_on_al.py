from ase.visualize import view
from ase.build import fcc100, add_adsorbate



a = 3.58

vac = 10
size_x = 5
size_y = 5
size_z = 2


slab_1 = fcc100(symbol='Al', a=a, vacuum=vac,
                      size=(size_x, size_y, size_z), periodic=True)


slab_2 = fcc100(symbol='Au', a=a,
                      size=(1, 1, 1), periodic=True)

add_adsorbate(slab=slab_1, adsorbate=slab_2, height=2.2,)


view(slab_1)