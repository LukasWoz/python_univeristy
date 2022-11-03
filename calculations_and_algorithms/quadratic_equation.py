
def roots_quadratic_equ(a, b, c):
    if a != 0:
        delta = b * b - 4 * a * c
        if delta > 0:
            delta_sq = delta ** (1 / 2)

            x1 = (-b + delta_sq) / (2 * a)
            x2 = (-b - delta_sq) / (2 * a)
            print("x1 = ", x1, "x2 = ", x2)
        elif delta == 0:
            x = -b / (2 * a)
            print("x = ", x)
        else:
            print(print("there are no real roots of the equation"))

    elif b != 0:
        x = -(c/b)
        print("x = ", x)
    else:
        print("there are no roots of the equation")


if __name__ == '__main__':
    roots_quadratic_equ(2, 8, 7)
