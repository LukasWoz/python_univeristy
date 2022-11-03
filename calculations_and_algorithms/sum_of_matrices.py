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


def matrix_add(matrix1, matrix2):
    print(matrix1)
    print(matrix2)
    if len(matrix1[0]) == len(matrix2[0]) and len(matrix1) == len(matrix2):
        n = len(matrix1)  # rows
        m = len(matrix1[0])  # columns
        m_sum = zeros_matrix(n, m)

        # iterate through rows
        for i in range(0, n):
            # iterate through columns
            for j in range(0, m):
                m_sum[i][j] = (matrix1[i][j] + matrix2[i][j])
        return m_sum
    else:
        print("matrices have different dimensions")


if __name__ == '__main__':
    print(matrix_add(random_matrix(128, 128), random_matrix(128, 128)))
