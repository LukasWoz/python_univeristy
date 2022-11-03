
class ComplexNumber:

    # Constructor
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag > 0:
            return str(self.real) + '+' + str(self.imag) + 'i'
        elif self.imag < 0:
            return str(self.real) + str(self.imag) + 'i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imag * other.imag),
                             (self.real * other.imag + other.real * self.imag))

    def __truediv__(self, other):
        div = (other.real * other.real) + (other.imag * other.imag)
        return ComplexNumber((self.real * other.real + self.imag * other.imag)/div,
                             (self.imag * other.real - self.real * other.imag)/div)

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    try:
        complex1real, complex1imag = map(int, input('Enter the first number (format: real_value imag_value):').split())
        complex2real, complex2imag = map(int, input('Enter the second number (format: real_value imag_value):').split())
        operator = input('Enter the operation you want to perform (e.g. "+", "-", "*", "/"):')
        complex1 = ComplexNumber(complex1real, complex1imag)
        complex2 = ComplexNumber(complex2real, complex2imag)
        if operator == '+':
            print(complex1 + complex2)
        elif operator == '-':
            print(complex1 - complex2)
        elif operator == '*':
            print(complex1 * complex2)
        elif operator == '/':
            print(complex1 / complex2)
        else: print('Wrong operator')

    except: print('Invalid input data format')


    """
    complex1 = ComplexNumber(2, 10)
    complex2 = ComplexNumber(3, 5)
    print(complex1 + complex2)
    print(complex1 - complex2)
    print(complex1 * complex2)
    print(complex1 / complex2)
    """


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
