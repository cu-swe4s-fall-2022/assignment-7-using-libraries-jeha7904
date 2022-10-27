from data_processor import get_random_matrix

from data_processor import get_file_dimensions

from data_processor import write_matrix_to_file

A = []
A = get_random_matrix(6,3)
print(A)

print(get_file_dimensions('iris.data'))

write_matrix_to_file(14, 6, 'random_data_test.data')