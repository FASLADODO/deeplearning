
'''
Federal University of Rio Grande do Norte

Prepare the data for input in the deep learning

https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/

csv_module.py
create at 28/05/2018

'''
import csv 
import sys

import numpy as np

'''
This if the function that read the csv file with the log to train the neural network

csv_file_name: the name of the csv file
columns: the columns of the csv file that will be returning
'''
def load_csv_data(csv_file_name, columns): 
	f = open(csv_file_name, 'rt')
	reader = csv.reader(f, delimiter=';')

	data = []

	for row in reader:
		col_number = 0	
		for col in row:
			if col_number in columns:
				data.append( row[col_number] )
			col_number += 1

	f.close()
	return data


