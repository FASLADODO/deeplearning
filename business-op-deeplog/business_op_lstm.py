

''' 
    https://github.com/keras-team/keras/issues/2045
    input data should be 3D tensor with shape (nb_samples, timesteps, input_dim).

    If I have 1000 sentences,each sentence has 10 words, and each word is presented in a 3-dim vector, so:
    1000 is nb_samples, 
    10 is the timesteps and 
    3 is the input_dim

    https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/

    to run:  

	execute the tensorflow emvoriment 

    cd tensorflow 
    source bin/activate

    python3 bussiness_op_lstm.py

'''

from __future__ import print_function

from numpy import array

from csv_module import load_csv_data
from csv_module import load_csv_data2
from array_module import reshape_input

from prepare_input_module import prepareLSTMdata
from process_learning_module import processLSTMLearning


# ==================== input values ====================

#macos
#raw_data_file_name = '/Users/jadson/Desktop/tinytrainingmock.csv';
#deep_network_file_name = '/Users/jadson/Desktop/trainingdata.csv';

#ubuntu
raw_data_file_name = '/home/jadson/Documentos/deeplog/csvs/tinytrainingmock2.csv';
deep_network_file_name = '/home/jadson/Documentos/deeplog/csvs/trainingdata.csv';

qtd_samples = 1 
qtd_timesteps = 10
qtd_features = 5
features_indexes = [0,1,2,3,5]
# ======================================================



# ==================== prepare LSTM data ===============


#prepareLSTMdata(raw_data_file_name, deep_network_file_name, features_indexes)

cvs_raw_data = load_csv_data2(deep_network_file_name)
#print(cvs_raw_data)

lstm_input_data = reshape_input(cvs_raw_data, qtd_samples, qtd_timesteps, qtd_features)
#print('### 4 ###')
#print(lstm_input_data)

lstm_input_label = [0.1]

# 5 features, 10 timesteps
lstm_test_data = array([
  [0.1, 1.0, 0.1, 1.0, 0.0],
  [0.2, 0.9, 0.1, 1.0, 0.0],
  [0.3, 0.8, 0.1, 1.0, 0.0],
  [0.4, 0.7, 0.1, 1.0, 0.0],
  [0.5, 0.6, 0.1, 1.0, 0.0],
  [0.6, 0.5, 0.1, 1.0, 0.0],
  [0.7, 0.4, 0.1, 1.0, 0.0],
  [0.8, 0.3, 0.1, 1.0, 0.0],
  [0.9, 0.2, 0.1, 1.0, 0.0],
  [1.0, 0.1, 0.1, 1.0, 0.0]])

lstm_test_data = reshape_input(lstm_test_data, qtd_samples, qtd_timesteps, qtd_features)

lstm_test_label =  [0.1]


# ==================== Process LSTM Model ===============


print('--- X_train ---')
print(lstm_input_data)
print(len(lstm_input_data))
print('--- y_train ---')
print(lstm_input_label)
print(len(lstm_input_label))


processLSTMLearning(lstm_input_data, lstm_input_label, lstm_test_data, lstm_test_label, qtd_timesteps, qtd_features)

