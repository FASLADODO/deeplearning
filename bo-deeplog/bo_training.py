
#python 
import numpy as np
from numpy import array



# my modules
from csv_module import load_traning_files
from csv_module import load_traning_output_files
from csv_module import load_test_files
from csv_module import load_test_output_files
from array_module import reshape_input

# my modules for deep learning funcions
from bo_module import buildLSTMModel1
from bo_module import buildLSTMModel2
from bo_module import traningLSTM


# ==================== input values ====================

#linux
base_directory          = '/home/jadson/git/deeplearning/data'
#macos
#base_directory           = '/Users/jadson/git/deeplearning/data'

training_directory      = base_directory+'/training'
tests_directory         = base_directory+'/tests'
model_file              = base_directory+'/lstm_model.h5'


# size of the data set
traning_samples = 518 
test_samples = 10
timesteps = 100
features = 1
classes = 10

#configuration of lstm 
lstm_layer_size = 100
dence_layer_size = 10
batch_size= 16
epochs=30

# ======================================================



# =============  LOAD THE TRANING DATA  FROM THE /data/training  ===============


print(' ------- loading traning data ------ ')
x_train = load_traning_files(training_directory, traning_samples)

x_train = reshape_input(x_train, traning_samples, timesteps, features)  # 256 samples x 100 timesteps x 1 features


print(' ------- loading traning output data ------ ')

y_train = load_traning_output_files(training_directory, traning_samples)  # 256 samples x 10 classes


# =============  LOAD THE TEST DATA FROM THE /data/tests  ===============

print(' ------- loading test data ------ ')
x_test = load_test_files(tests_directory, test_samples)  #  100 timesteps x 1 feature

x_test = reshape_input(x_test, test_samples, timesteps, features) # 10 samples x 100 timesteps x 1 feature

print(' ------- loading test output data ------ ')

y_test = load_test_output_files(tests_directory)  # 10 classes x 10 samples



# ==================== Process LSTM Model ===============


#print('--- X_train ---')
#print(x_train)
#print(len(x_train))
#print('--- y_train ---')
#print(y_train)
#print(len(y_train))


model = buildLSTMModel1(lstm_layer_size, dence_layer_size, timesteps, features)

traningLSTM(model, batch_size, epochs, np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test) )

# ==================== Save the Model ===============

# save model to single file
# sudo pip install h5py
model.save(model_file)
