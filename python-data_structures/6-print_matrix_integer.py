#!/urs/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mem1 in range(len(matrix)):
        for mem in range(len(matrix[mem1])):
            if mem != len(matrix[mem]) - 1:
                print("{:d} ".format(matrix[mem1][mem]), end="")
            else:
                print("{:d}".format(matrix[mem1][mem]), end="")
        print()
