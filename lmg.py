# Light Mediated Growth Simulation Software
# Main File

import numpy,scipy.io,h5py,sys

def openMatFile(fileName):
    """Open matlab (.mat) file.
    Returns dict if version < 7.3 or HDF5 file if version == 7.3"""
    try:
        return scipy.io.loadmat(fileName)
    except NotImplementedError:
        return h5py.File(fileName)
        

a=openMatFile('iteration30.mat')
#a=openMatFile('setup_parameters.mat')


for key in a.keys():
    print key
    print(a[key])
    

# Load setup parameters

# Load other variables

## Loop over iteration numbers

# Identify Iteration

# Add Mass

# Remove Mass

# Write Structure

## End Loop


print('Completed Successfully!')
#exit()