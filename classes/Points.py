#!/usr/bin/env python3

# Class 2 - Find the Torsional Angle
# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        # dot product = (Ax*Bx) + (Ay*By) + (Az*Bz)
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        # cross product = ((Az*Bz)*(AzBy), (Az*Bx)*(AxBz), (Ax*By)*(AyBx))
        x = (self.y * no.z) - (self.z * no.y)
        y = (self.z * no.x) - (self.x * no.z)
        z = (self.x * no.y) - (self.y * no.x)
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == "__main__":
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = (
        Points(*points[0]),
        Points(*points[1]),
        Points(*points[2]),
        Points(*points[3]),
    )
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
