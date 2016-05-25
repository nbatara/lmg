# Light Mediated Growth Simulation Software
# Main File

import numpy
import scipy.io
import h5py
import sys
import time


def open_mat_file(file_name):
    """Open matlab (.mat) file.
    Returns dict if version < 7.3 or HDF5 file if version == 7.3"""
    try:
        return scipy.io.loadmat(file_name)
    except NotImplementedError:
        return h5py.File(file_name)


def circ_shift(numpy_array, shift_coord):
    """ circ_shift(numpy_array,shift_coord)..
    Shift contents of numpy array circularly. Returns array of same type"""
    shift_coord = numpy.array(shift_coord)*-1
    
    if len(shift_coord) == 2:
        return numpy.concatenate((numpy.concatenate((numpy_array[shift_coord[0]:, shift_coord[1]:], numpy_array[shift_coord[0]:, :shift_coord[1]]), 1), numpy.concatenate((numpy_array[:shift_coord[0], shift_coord[1]:], numpy_array[:shift_coord[0], :shift_coord[1]]), 1)), 0)
    
    if len(shift_coord) == 3:
        a = numpy.concatenate((numpy_array[shift_coord[0]: , shift_coord[1]: , shift_coord[2]:] , numpy_array[shift_coord[0]: , shift_coord[1]: , :shift_coord[2]]),2)
        b = numpy.concatenate((numpy_array[shift_coord[0]: , :shift_coord[1] , shift_coord[2]:] , numpy_array[shift_coord[0]: , :shift_coord[1] , :shift_coord[2]]),2)
        c = numpy.concatenate((a, b), 1)
        d = numpy.concatenate((numpy_array[:shift_coord[0] , shift_coord[1]: , shift_coord[2]:] , numpy_array[:shift_coord[0] , shift_coord[1]: , :shift_coord[2]]),2)
        e = numpy.concatenate((numpy_array[:shift_coord[0] , :shift_coord[1] , shift_coord[2]:] , numpy_array[:shift_coord[0] , :shift_coord[1] , :shift_coord[2]]),2)
        f = numpy.concatenate((d, e), 1)
        h = numpy.concatenate((c, f), 0)
        return h


def sum_array_neighbors(numpy_array, neighbor_coordinates):
    """ sum_array_neighbors(numpy_array,neighbor_coordinates):
    Sums the values of an array at relative positions specified in neighbor_coordinates."""
    neighbor_coordinates = numpy.array(neighbor_coordinates)
    output = numpy.zeros(numpy_array.shape, 'int8')
    for subCoord in neighbor_coordinates:
        output = output+circ_shift(numpy_array, subCoord)
    return output


# Test CircShift

# arraySize=int(1e2)
# a=numpy.random.randint(2,size=(arraySize,arraySize,arraySize))
# a=numpy.array(a,'uint8')

# time1=time.time()
# for x in xrange(1):
    # b1=numpy.roll(numpy.roll(numpy.roll(a,3,0),3,1),-2,2)
# print  str(time.time()-time1) + 's to complete roll'

# time2=time.time()
# for x in xrange(1):
    # b2=circ_shift(a,[3,3,-2])

# print  str(time.time()-time2) + 's to complete circshift'

# a=open_mat_file('iteration30.mat')
# a=open_mat_file('setup_parameters.mat')


# for key in a.keys():
    # print key
    # print(a[key])
    

# Main Execution Block

# Load setup parameters

# Load other variables

# Loop over iteration numbers

# Identify Iteration

# Add Mass

# Remove Mass

# Write Structure

# End Loop


print('Completed Successfully!')
# exit()
