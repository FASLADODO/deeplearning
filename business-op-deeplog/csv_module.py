
'''
Federal University of Rio Grande do Norte

Prepare the log data for input in the deep learning



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
def load_csv_data(csv_file_name, included_cols):
	
	data = []

	with open(csv_file_name) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		for row in readCSV:
			for col in included_cols:
				data.append(row[col])		

	#print(data)    	
	return data


def load_csv_data2(csv_file_name):
	
	data = []

	with open(csv_file_name) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		for row in readCSV:
			data.append(row)
	#print(data)    	
	return data	


'''
   write the data pre processed to the temp file 
'''
def save_csv_data(csv_file_name, cvs_data, qtd_feature):

    with open(csv_file_name,'w') as resultFile:
    	wr = csv.writer(resultFile, delimiter=';', dialect='excel')

    	qtd_rows =  int( len(cvs_data) / qtd_feature)
    	for row_number in range( qtd_rows ):
    		row = []
    		for column_number in range( qtd_feature ):
    			row.append( cvs_data[   (row_number * qtd_feature ) + column_number] )

    		wr.writerow(row)


