#
# 
# http://nghiaho.com/?p=2333 
#
# To run this example, install modules:
# 
# pip3 install numpy scipy
# pip3 install scikit-learn
# pip3 install pillow
# pip3 install h5py
#

from keras.models import Sequential
from keras.utils import np_utils
from keras.layers.core import Dense, Activation, Dropout


import numpy as np
import os.path

#
# The CSV files are converted to native Numpy binary for subsequent 
# loading because it is much faster than parsing CSV
#
if not os.path.isfile("trainingmock.npy"):
    traincsv = np.loadtxt('trainingmock.csv', delimiter=';', dtype=np.str)
    np.save('trainingmock.npy', traincsv);
else:
    train = np.load('trainingmock.npy')

labels = np.ones((train.shape[0], 1), dtype=int);

print (" shape[0] : ", train.shape[0])
print (" shape    : ", train.shape)
print (" labels   : ", labels)
