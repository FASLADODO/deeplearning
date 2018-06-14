

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Activation, Flatten
from keras.layers import LSTM
from keras.datasets import imdb



def processLSTMLearning(lstm_input_data, lstm_input_label, lstm_test_data, lstm_test_label, qtd_timesteps, qtd_features):

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
	model.add( LSTM(10, input_shape=(qtd_timesteps, qtd_features), return_sequences=True ) )
	model.add( LSTM(10, return_sequences=True) )
	model.add( LSTM(10, return_sequences=True) )

	#The problem is that you start with a three dimensional layer but 
	#never reduce the dimensionality in any of the following layers.
	#Try adding mode.add(Flatten()) before the last Dense layer
	#
	# https://github.com/keras-team/keras/issues/6351
	#
	model.add(Flatten())

	# full conected layer a "normal" neural network
	#model.add(Dense(128, activation='relu'))
	model.add(Dense(1, activation='softmax'))


	# try using different optimizers and different optimizer configs
	model.compile(loss='sparse_categorical_crossentropy',
	              optimizer='adam',
	              metrics=['accuracy'])


	# ===================== Train LSTM  ===================

	# with validation data
	#model.fit(lstm_input_data, lstm_input_label,
	#          batch_size=batch_size,
	#          epochs=1,
	#          validation_data=(lstm_test_data, lstm_test_data))

	# without validation data
	model.fit(lstm_input_data, lstm_input_label, epochs=10, batch_size=1)

	#score, acc = model.evaluate(lstm_test_data, lstm_test_data,
	#                            batch_size=batch_size)
	#print('Test score:', score)
	#print('Test accuracy:', acc)

	scores = model.evaluate(lstm_test_data, lstm_test_label, verbose=0)
	print("Accuracy: %.2f%%" % (scores[1]*100))




