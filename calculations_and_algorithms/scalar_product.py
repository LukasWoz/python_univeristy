
def scalar_product(a, b):
    if len(a) == len(b):
        scalar = 0
        for i in range(0, len(a)):
            scalar += a[i] * b[i]
        return scalar
    else: print("vectors vary in length")


if __name__ == '__main__':
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    print(scalar_product(a, b))
