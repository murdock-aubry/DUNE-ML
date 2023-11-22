# To download a file off compute Canada, run the following line of code in the command line:
#
#   scp [username]@cedar.computecanada.ca:projects/rpp-nilic/neutrino_ml/MCprodW/[file name] /path/to/destination/on/local
#

import h5py
import numpy as np

f = h5py.File("NeutrinoML_r00725_s00000_ts868829.h5")


keys = np.array(f.keys())
print(keys)

print(f['edep_table']['energy'][()])
