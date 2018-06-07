

from numpy import array

'''
  This method normalize the values of the features betwenn 0 and 1 values
'''
def normalize_input(cvs_3D_data, samples, features):
  for feature_number in range( features ):
      return normalize_feature(cvs_3D_data, samples, feature_number)


def normalize_feature(cvs_3D_data, samples, feature_number): 
    # for each example
    for sample in range( samples ):

        # normaliza the values of one feature
        bigger = 0
        smaller = 0 
        
        for value in range( len(cvs_3D_data[sample]) ):
            data = cvs_3D_data[sample][value][feature_number]
            if bigger < data:
                bigger = data
            if smaller == 0 or  smaller > data:
                smaller = data
            cvs_3D_data[sample][value][feature_number]

        for value in range( len(cvs_3D_data[sample]) ):
            data = cvs_3D_data[sample][value][feature_number]
            cvs_3D_data[sample][value][feature_number] = normalize (data, smaller, bigger )
                
    return cvs_3D_data


def normalize(data, smaller, bigger): 
    data = (data - smaller) /  ( bigger - smaller )
    return data
