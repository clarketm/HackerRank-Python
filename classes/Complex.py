#!/usr/bin/env python3


# Classes: Dealing with Complex Numbers
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        _complex = complex(self.real, self.imaginary) + complex(no.real, no.imaginary)
        return Complex(_complex.real, _complex.imag)

    def __sub__(self, no):
        _complex = complex(self.real, self.imaginary) - complex(no.real, no.imaginary)
        return Complex(_complex.real, _complex.imag)

    def __mul__(self, no):
        _complex = complex(self.real, self.imaginary) * complex(no.real, no.imaginary)
        return Complex(_complex.real, _complex.imag)

    def __truediv__(self, no):
        _complex = complex(self.real, self.imaginary) / complex(no.real, no.imaginary)
        return Complex(_complex.real, _complex.imag)

    def mod(self):
        _complex = complex(math.sqrt(self.real ** 2 + self.imaginary ** 2))
        return Complex(_complex.real, _complex.imag)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
