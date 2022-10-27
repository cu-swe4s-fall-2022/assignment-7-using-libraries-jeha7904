# remember to import your libraries!
import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):
    random_matrix = np.random.rand(num_rows,num_columns)
    return random_matrix

def get_file_dimensions(file_name):
    file_data = pd.read_csv(file_name, header=None)
    file_shape = file_data.shape
    return (file_shape[0],file_shape[1])

def write_matrix_to_file(num_rows, num_columns, file_name):
    random_matrix = get_random_matrix(num_rows, num_columns)
    np.savetxt(file_name, random_matrix, delimiter=",")
    return None