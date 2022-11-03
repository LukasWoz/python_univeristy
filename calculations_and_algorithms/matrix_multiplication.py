import random


def zeros_matrix(size1, size2):
    matrix = []

    for j in range(size1):
        matrix.append([])
        for i in range(size2):
            matrix[j].append(0)
    return matrix


def random_matrix(size1, size2):

    matrix = []
    for j in range(size1):
        matrix.append([])
        for i in range(size2):
            matrix[j].append(random.randint(0,100))

    return matrix


def matrix_multiplic(matrix1, matrix2):
    print(matrix1)
    print(matrix2)
    n1 = len(matrix1)  # rows in matrix1
    m1 = len(matrix1[0])  # columns in matrix1
    n2 = len(matrix2)  # rows in matrix2
    m2 = len(matrix2[0])  # columns in matrix2
    if m1 == n2:
        m_mult = zeros_matrix(n1,m2)

        # iterate through rows
        for i in range(n1):
            # iterate through columns
            for j in range(m2):
                for k in range(m1):
                    m_mult[i][j] += (matrix1[i][k] * matrix2[k][j])
        return m_mult
    else:
        print("these matrices cannot be multiplied")


if __name__ == '__main__':
    print(matrix_multiplic(random_matrix(8, 8), random_matrix(8, 8)))
