def roots_quadratic_equ(a, b, c):
    x = []
    if a != 0:
        delta = b * b - 4 * a * c
        if delta > 0:
            delta_sq = delta ** (1 / 2)

            x1 = round((-b + delta_sq) / (2 * a), 2)
            x2 = round((-b - delta_sq) / (2 * a), 2)
            x.append(x1)
            x.append(x2)
            # print("x1 = ", x1, "x2 = ", x2)
        elif delta == 0:
            x1 = round(-b / (2 * a), 2)
            x.append(x1)
            # print("x = ", x)
        else:
            print(print("there are no real roots of the equation"))

    elif b != 0:
        x1 = round(-(c/b), 2)
        x.append(x1)
        # print("x = ", x)
    else:
        print("there are no roots of the equation")
    return x

if __name__ == '__main__':
    print(roots_quadratic_equ(2, 8, 7))