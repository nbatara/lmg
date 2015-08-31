# Light Mediated Growth Simulation Software
# Main File


import numpy, scipy.io, h5py , sys, time

def openMatFile(fileName):
    """Open matlab (.mat) file.
    Returns dict if version < 7.3 or HDF5 file if version == 7.3"""
    try:
        return scipy.io.loadmat(fileName)
    except NotImplementedError:
        return h5py.File(fileName)

def circShift(numpyArray,shiftCoord):
    """ circShift(numpyArray,shiftCoord)..
    Shift contents of numpy array circularly. Returns array of same type"""
    shiftCoord=numpy.array(shiftCoord)*-1
    
    if len(shiftCoord)==2:
        return numpy.concatenate((numpy.concatenate((numpyArray[shiftCoord[0]: , shiftCoord[1]:] , numpyArray[shiftCoord[0]: , :shiftCoord[1]]),1),numpy.concatenate((numpyArray[:shiftCoord[0] , shiftCoord[1]:] , numpyArray[:shiftCoord[0] , :shiftCoord[1]]),1)),0)
    
    if len(shiftCoord)==3:
        a=numpy.concatenate((numpyArray[shiftCoord[0]: , shiftCoord[1]: , shiftCoord[2]:] , numpyArray[shiftCoord[0]: , shiftCoord[1]: , :shiftCoord[2]]),2)
        b=numpy.concatenate((numpyArray[shiftCoord[0]: , :shiftCoord[1] , shiftCoord[2]:] , numpyArray[shiftCoord[0]: , :shiftCoord[1] , :shiftCoord[2]]),2)
        c=numpy.concatenate((a,b),1)
        d=numpy.concatenate((numpyArray[:shiftCoord[0] , shiftCoord[1]: , shiftCoord[2]:] , numpyArray[:shiftCoord[0] , shiftCoord[1]: , :shiftCoord[2]]),2)
        e=numpy.concatenate((numpyArray[:shiftCoord[0] , :shiftCoord[1] , shiftCoord[2]:] , numpyArray[:shiftCoord[0] , :shiftCoord[1] , :shiftCoord[2]]),2)
        f=numpy.concatenate((d,e),1)
        h=numpy.concatenate((c,f),0)
        return h
    
def sumArrayNeighbors(numpyArray,neighborCoordinates):
    """ sumArrayNeighbors(numpyArray,neighborCoordinates):
    Sums the values of an array at relative positions specified in neighborCoordinates. Returns uint8 array unless    """
    neighborCoordinates=numpy.array(neighborCoordinates)
    output=numpy.zeros(numpyArray.shape,'int8')
    for subCoord in neighborCoordinates:
        output=output+circShift(numpyArray,subCoord)
    return output
        

## Test CircShift        

#arraySize=int(1e2)        
#a=numpy.random.randint(2,size=(arraySize,arraySize,arraySize))
#a=numpy.array(a,'uint8')

#time1=time.time()
#for x in xrange(1):
    #b1=numpy.roll(numpy.roll(numpy.roll(a,3,0),3,1),-2,2)
#print  str(time.time()-time1) + 's to complete roll'

#time2=time.time()
#for x in xrange(1):
    #b2=circShift(a,[3,3,-2])

#print  str(time.time()-time2) + 's to complete circshift'





# a=openMatFile('iteration30.mat')
#a=openMatFile('setup_parameters.mat')


#for key in a.keys():
    #print key
    #print(a[key])
    

###Main Execution Block

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
