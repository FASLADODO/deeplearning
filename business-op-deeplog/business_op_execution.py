
from numpy import array
from keras.models import load_model

from array_module import reshape_input


#macos
raw_data_file_name     = '/Users/jadson/Desktop/tinytrainingmock.csv'
deep_network_file_name = '/Users/jadson/Desktop/trainingdata.csv'
businnes_op_lstm_model = '/Users/jadson/Desktop/final_model.h5'

#ubuntu
#raw_data_file_name      = '/home/jadson/Documentos/deeplog/csvs/tinytrainingmock2.csv'
#deep_network_file_name  = '/home/jadson/Documentos/deeplog/csvs/trainingdata.csv'
#businnes_op_lstm_model  = '/home/jadson/Documentos/deeplog/csvs/final_model.h5'


# load model from single file
model = load_model(businnes_op_lstm_model)


x = array([
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

x = reshape_input(x, 1, 10, 5)

# make predictions
#yhat = model.predict(x, verbose=0)
yhat = model.predict_classes(x, verbose=0)
print(yhat)