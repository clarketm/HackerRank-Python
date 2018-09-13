from math import gcd

p, q = map(int, input().split())
n = p * q
phi = (p - 1) * (q - 1)
min = 9999999999999
sum_e = 0

for e in range(3, phi, 2):
    if gcd(e, phi) != 1:
        continue
    num_unconcealed = (gcd(e - 1, p - 1) + 1) * (gcd(e - 1, q - 1) + 1)
    if num_unconcealed < min:
        min = num_unconcealed
        sum_e = e
    elif num_unconcealed == min:
        sum_e += e

print(sum_e % ((10**9) + 7))

# s, e = 0, 3
# phi = (p - 1) * (q - 1)
#
# while e < phi:
#     if gcd(e, phi) == 1 and gcd(e - 1, q - 1) == 2 and gcd(e - 1, p - 1) == 2:
#         s += e
#     e += 4
#
# print(s % ((10 ** 9) + 7))
