


from csv_module import load_csv_data

#from bo_input_module import prepared

cvs_raw_data = load_csv_data('/home/jadson/Documentos/deeplog/csvs/trainingmock.csv', [0,1,2,3,5]);
print(cvs_raw_data)
print(len(cvs_raw_data))


''' 
    https://github.com/keras-team/keras/issues/2045
    input data should be 3D tensor with shape (nb_samples, timesteps, input_dim).

    If I have 1000 sentences,each sentence has 10 words, and each word is presented in a 3-dim vector, so:
    1000 is nb_samples, 
    10 is the timesteps and 
    3 is the input_dim


    https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/


'''