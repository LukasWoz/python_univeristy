import numpy as np
import matplotlib.pyplot as plt
from multiprocessing.pool import Pool


def square_matrix_det(size):
    m = np.random.rand(size, size)
    x = np.linalg.det(m)
    return x


if __name__ == "__main__":
    p = Pool(processes=4)

    result = p.map(square_matrix_det, (2*x for x in range(5)))

    p.close()   # closes a pipe which informs readers of that pipe,
    # that there will be no more data coming through it.

    p.join()    # waits for a child process to be killed

    plt.hist(result, bins=10)
    plt.show()
