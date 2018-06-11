

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
from csv_module import load_csv_data2
#from hash_module import textual_hash
#from hash_module import date_milliseconds
#from normalization_module import normalize_feature
from array_module import reshape_input

from prepare_input_module import prepareLSTMdata

# ==================== input values ====================


raw_data_file_name = '/Users/jadson/Desktop/tinytrainingmock.csv';
#raw_data_file_name = '/home/jadson/Documentos/deeplog/csvs/tinytrainingmock2.csv';

deep_network_file_name = '/Users/jadson/Desktop/trainingdata.csv';
#deep_network_file_name = '/home/jadson/Documentos/deeplog/csvs/trainingdata.csv';

qtd_samples = 1 
qtd_timesteps = 5
qtd_features = 5
features_indexes = [0,1,2,3,5]
# ======================================================


prepareLSTMdata(raw_data_file_name, deep_network_file_name, features_indexes)

cvs_raw_data = load_csv_data2(deep_network_file_name)
print(cvs_raw_data)

cvs_3D__input_data = reshape_input(cvs_raw_data, qtd_samples, qtd_timesteps, qtd_features)
print('### 4 ###')
print(cvs_3D__input_data)








