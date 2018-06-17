

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Activation, Flatten
from keras.layers import LSTM
from keras.datasets import imdb


def buildLSTMModel(lstm_layer_size, dence_layer_size, timesteps, data_dim):


	model = Sequential()

	# The LSTM layer with 10 blocks
	#
	# The three dimensions of this input are:
	#
	# *** Samples ***    : One sequence is one sample. A batch is comprised of one or more samples.
	# *** Time Steps *** : One time step is one point of observation in the sample.
	# *** Features ***   : One feature is one observation at a time step.
	#
	# the network assumes you have 1 or more samples 
	# and requires that you specify the number of time steps and the number of features.
	#
	# return_sequences=True    What this does is ensure that the LSTM cell returns all of 
	#                          the outputs from the unrolled LSTM cell through time.
	#
	model.add( LSTM(lstm_layer_size, return_sequences=True, input_shape=(timesteps, data_dim) ) )
	model.add( LSTM(lstm_layer_size, return_sequences=True) )
	model.add( LSTM(lstm_layer_size) )

	# full conected layer a "normal" neural network
	#model.add(Dense(128, activation='relu'))
	model.add(Dense(dence_layer_size, activation='softmax'))

	return model;


def processLSTMLearning(model, batch_size, epochs, x_train, y_train, x_val, y_val, x_test, y_test):


	# try using different optimizers and different optimizer configs
	# loss:
	# https://en.wikipedia.org/wiki/Loss_function
	# http://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html
	# optimizer:
	# http://ruder.io/optimizing-gradient-descent/index.html#rmsprop
	#
	model.compile(loss='categorical_crossentropy',
	              optimizer='rmsprop',
	              metrics=['accuracy'])


	# ===================== Train LSTM  ===================

	# with validation data
	#model.fit(lstm_input_data, lstm_input_label,
	#          batch_size=batch_size,
	#          epochs=1,
	#          validation_data=(lstm_test_data, lstm_test_data))

	# without validation data
	model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_val, y_val) )

    
	#score, acc = model.evaluate(lstm_test_data, lstm_test_data,
	#                            batch_size=batch_size)
	#print('Test score:', score)
	#print('Test accuracy:', acc)

	scores = model.evaluate(x_test, y_test, verbose=0)
	print("Accuracy: %.2f%%" % (scores[1]*100))




