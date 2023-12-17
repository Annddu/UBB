# Solve the problem from the first set here
# For a given natural number n find the largest natural number written with the same digits. (e.g. n=3658, m=8653).


def largestnaturalnumber(n):
    digits = list(str(n))
    digits.sort(reverse=True)
    m = int(''.join(digits))
    return m

n = input("Enter an number: ")
print(largestnaturalnumber(n))