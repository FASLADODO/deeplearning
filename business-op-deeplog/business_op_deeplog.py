

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
from hash_module import textual_hash
from hash_module import date_milliseconds
from normalization_module import normalize_feature
from array_module import reshape_input


# ==================== input values ====================
#input_file = '/Users/jadson/Desktop/tinytrainingmock.csv';
input_file = '/home/jadson/Documentos/deeplog/csvs/tinytrainingmock2.csv';

qtd_samples = 1 
qtd_timesteps = 2
qtd_features = 5
features_indexes = [0,1,2,3,5]
# ======================================================

# load just the feature located in this possition on cvs file
cvs_raw_data = load_csv_data(input_file, features_indexes)

print(cvs_raw_data)
print('-----------------------------------')

# converte the url to numeric value
cvs_numeric_data = textual_hash(cvs_raw_data, 3, qtd_features)

print(cvs_numeric_data)
print('-----------------------------------')

# converte the date to numeric value
cvs_numeric_data = date_milliseconds(cvs_numeric_data, 2, qtd_features)

print(cvs_numeric_data)
print('-----------------------------------')

cvs_normalized_data = []

for feature in range( len(cvs_numeric_data) ):
    cvs_normalized_data = normalize_feature(cvs_numeric_data, feature, qtd_features)

print(cvs_normalized_data)


cvs_3D__input_data = reshape_input(cvs_raw_data, qtd_samples, qtd_timesteps, qtd_features)
print(cvs_3D__input_data)

'''
cvs_3D_data = reshape_input(cvs_raw_data, samples, timesteps, features)
print(cvs_3D_data)
print('-----------------------------------')
print(cvs_3D_data[0])
print('-----------------------------------')
print(cvs_3D_data[0][0])
print('-----------------------------------')
print(cvs_3D_data[0][0][0])
print(cvs_3D_data[0][4][0])


'''

