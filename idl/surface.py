from ase.build import bcc100, bcc111, bcc110, add_adsorbate
from ase.visualize import view



a = 3.6

structs = []

struct1 =  bcc100(symbol='Cu', size=(2, 2, 4), a=a, vacuum=5)
struct2 =  bcc111(symbol='Cu', size=(2, 2, 4), a=a, vacuum=5)
struct3 =  bcc110(symbol='Cu', size=(2, 2, 4), a=a, vacuum=5)


structs.append(struct1)
structs.append(struct2)
structs.append(struct3)



view(structs)