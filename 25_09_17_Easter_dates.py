"""This code predicts the date of easter in the given year"""
year = int(input("Enter year: "))

a = year % 19
b = year % 4
c = year % 7

k = year // 100
p = (13 + 8 * k) // 25  # fixed (1816), was: k // 3
q = k // 4
M = (15 - p + k - q) % 30
N = (4 + k - q) % 7

d = (19 * a + M) % 30
e = (2 * b + 4 * c + 6 * d + N) % 7
march_easter = d + e + 22
april_easter = d + e - 9

if april_easter == 25 and d == 28 and e == 6 and a > 10:  # changed (1807), was: (11 * M + 11) % 30 < 19
    april_easter = 18

if april_easter == 26 and d == 29 and e == 6:
    april_easter = 19

if march_easter <= 31:
    print(march_easter, "March")
else:
    print(april_easter, "April")
