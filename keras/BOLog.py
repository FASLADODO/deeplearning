


from bo_log_csv_module import load_data

from bo_input_module import prepared

data_train = load_data('/Users/jadson/Desktop/trainingmock.csv', [0,2,3,4]);
print(data_train)
print(len(data_train))


''' 
    https://github.com/keras-team/keras/issues/2045
    input data should be 3D tensor with shape (nb_samples, timesteps, input_dim).

    If I have 1000 sentences,each sentence has 10 words, and each word is presented in a 3-dim vector, so:
    1000 is nb_samples, 
    10 is the timesteps and 
    3 is the input_dim


    https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/


'''