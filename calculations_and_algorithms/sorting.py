import random


def descending_sort(numbers):

    print(numbers)
    n = len(numbers)
    while n > 1:
        change = False
        for i in range(0, n - 1):
            if numbers[i]<numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                change = True

        n -= 1
        #print(numbers)
        if change == False: break

    return numbers


def random_numbers(size):
    i = 0
    numbers = []
    while i < size:
        i += 1
        numbers.append(random.randint(0, 100))
    return numbers


if __name__ == '__main__':
    print(descending_sort(random_numbers(50)))
