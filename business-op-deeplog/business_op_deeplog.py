

''' 
    https://github.com/keras-team/keras/issues/2045
    input data should be 3D tensor with shape (nb_samples, timesteps, input_dim).

    If I have 1000 sentences,each sentence has 10 words, and each word is presented in a 3-dim vector, so:
    1000 is nb_samples, 
    10 is the timesteps and 
    3 is the input_dim


    https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/


'''


from csv_module import load_csv_data
from array_module import reshape_input
from normalization_module import normalize_input

# ==================== input values ====================
input_file = '/Users/jadson/Desktop/tinytrainingmock.csv';
#input_file = '/home/jadson/Documentos/deeplog/csvs/trainingmock.csv';

samples = 1 
timesteps = 5
features = 5
# ======================================================

cvs_raw_data = load_csv_data(input_file, [0,1,2,3,5])


cvs_3D_data = reshape_input(cvs_raw_data, samples, timesteps, features)
print(cvs_3D_data)
print('-----------------------------------')
print(cvs_3D_data[0])
print('-----------------------------------')
print(cvs_3D_data[0][0])
print('-----------------------------------')
print(cvs_3D_data[0][0][0])
print(cvs_3D_data[0][4][0])


cvs_3D_normalized_data = normalize_input(cvs_3D_data, samples, features)
print(cvs_3D_normalized_data)


