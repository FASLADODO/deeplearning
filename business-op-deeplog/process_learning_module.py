

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
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
	model.add(LSTM(10, input_shape=(qtd_timesteps, qtd_features) ) )

	# full conected layer a "normal" neural network
	model.add(Dense(1, activation='sigmoid'))


	# try using different optimizers and different optimizer configs
	model.compile(loss='binary_crossentropy',
	              optimizer='adam',
	              metrics=['accuracy'])


	# ===================== Train LSTM  ===================

	# with validation data
	#model.fit(lstm_input_data, lstm_input_label,
	#          batch_size=batch_size,
	#          epochs=1,
	#          validation_data=(lstm_test_data, lstm_test_data))

	# without validation data
	model.fit(lstm_input_data, lstm_input_label, epochs=3, batch_size=64)

	#score, acc = model.evaluate(lstm_test_data, lstm_test_data,
	#                            batch_size=batch_size)
	#print('Test score:', score)
	#print('Test accuracy:', acc)

	scores = model.evaluate(lstm_test_data, lstm_test_label, verbose=0)
	print("Accuracy: %.2f%%" % (scores[1]*100))