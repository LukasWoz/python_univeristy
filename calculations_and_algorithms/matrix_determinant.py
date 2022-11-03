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


def matrix_determinant(matrix, det_total=0):
    n = len(matrix)
    m = len(matrix[0])
    if n == m:
        indexes = list(range(n))
        if n == 2 and m == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return det

        for c in indexes:
            matrix_cp = matrix
            matrix_cp = matrix[1:]  # remove first row
            n = len(matrix_cp)
            for i in range(n):
                matrix_cp[i] = matrix_cp[i][0:c] + matrix_cp[i][c+1:]

            sign = (-1) ** (c % 2)
            sub_det = matrix_determinant(matrix_cp)
            det_total += sign * matrix[0][c] * sub_det

        return det_total

    else:
        print("Matrix must be square")


if __name__ == '__main__':
    m = random_matrix(4, 4)
    print(m)
    print(matrix_determinant(m))
