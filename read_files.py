# To download a file off compute Canada, run the following line of code in the command line:
#
#   scp [username]@cedar.computecanada.ca:projects/rpp-nilic/neutrino_ml/MCprodW/[file name] /path/to/destination/on/local
#
# The most fundamental thing to remember when using h5py is: Groups work like dictionaries, and datasets work like NumPy arrays

import h5py
import numpy as np
import matplotlib.pyplot as plt


#Open the file
f = h5py.File("NeutrinoML_r00725_s00000_ts868829.h5")
print(type(f))


#What is stored in this file? h5py.File acts like a python dictionary, thus we can check the keys
keys = np.array(f.keys())

# print(keys)
# print(f['hit_table'].keys())

hit_event = f['hit_table']['event_id'][()]

print(max(abs(hit_event[:, 1])))
# print(len(f['hit_table']['event_id'][()][:, 0]))


# print(f['event_table']['nu_dir'][()])
# print(f['event_table']['lep_energy'][()])
quit()

#We can see that there are 5 major groups
print(keys)
#We can check one of them
print(type(f['edep_table']))

#In this case, we have sub-groups that will act like python dictionaries, so we can check the keys of these sub-groups. Lets try the sub-group f['edep_table']
edep_table = f['edep_table']
keys_edep_table = np.array(edep_table.keys())
print(keys_edep_table)

#Now we have reached a few datasets within f['edep_table'], we can check one of them
print(type(f['edep_table']['energy']))
#Datasets act like NumPy arrays
print(np.size(f['edep_table']['energy'][()]))

#Now lets plot one of these datasets
x = np.linspace(0, 1, np.size(f['edep_table']['energy'][()]))
plt.plot(x, f['edep_table']['energy'][()])
plt.show()



#Feel use the space below to open more files or play around with the existing one

#f = h5py.File("File_Name")