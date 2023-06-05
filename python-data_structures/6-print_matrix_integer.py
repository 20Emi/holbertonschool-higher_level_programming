#!/urs/bin/python3
def print_matrix_integer(matrix=[[]]):
    for member in range(len(matrix)):
        for mem in range(len(matrix[member])):
            if mem != len(matrix[member]) - 1:
                print("{:d} ".format(matrix[member][mem]), end='')
            else:
                print("{:d}".format(matrix[member][mem]), end='')
        print()
