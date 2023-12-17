# Dynamic programing
# 6. Given an array of integers A, maximize the value of the expression A[m] - A[n] + A[p] - A[q], where m, n, p, q are array indices with m > n > p > q. 
# For A = [30, 5, 15, 18, 30, 40], the maximum value is 32, obtained as 40 - 18 + 15 - 5. 
# Display both the maximum value as well as the expression used to calculate it. (display data structure, explain it)
import sys

def read_sequence ():
    string = input("Enter an list: ")
    print()
    import re
    return [int(s) for s in re.findall(r"-?\d+", string)]

def naive(A):
    print("Naive method")
    am = 0
    an = 0
    ap = 0
    aq = 0
    max_ex = -sys.maxsize
    for m in reversed(range(len(A))):
        for n in reversed(range(m)):
            for p in reversed(range(n)):
                for q in reversed(range(p)):
                    if (A[m] - A[n] + A[p] - A[q]) > max_ex:
                        max_ex = A[m] - A[n] + A[p] - A[q]
                        am = A[m]
                        an = A[n]
                        ap = A[p]
                        aq = A[q]
    print(f"The maximum value is: {max_ex}")
    print(f"The expression is: {am} - {an} + {ap} - {aq}")
    print()
 
def dynamic(A):
    print("Dynamic programming method")
    # we store the smallest possible value 
    array1 = [-sys.maxsize] * (len(A) + 1)
    array2 = [-sys.maxsize] * len(A)
    array3 = [-sys.maxsize] * (len(A) - 1)   
    array4 = [-sys.maxsize] * (len(A) - 2)

    # A[m]
    for i in reversed(range(len(A))):
        array1[i] = max(array1[i + 1], A[i])
 
    # A[m] - A[n]
    for i in reversed(range(len(A) - 1)):
        array2[i] = max(array2[i + 1], array1[i + 1] - A[i])
 
    # A[m] - A[n] + A[p]
    for i in reversed(range(len(A) - 2)):
        array3[i] = max(array3[i + 1], array2[i + 1] + A[i])
 
    # A[m] - A[n] + A[p] - A[q]
    for i in reversed(range(len(A) - 3)):
        array4[i] = max(array4[i + 1], array3[i + 1] - A[i])
    
    print("The first expression memorise the maximum element A[m] from right to left:")
    print(array1)
    print()
    print("The second expression memorise the maximum of A[m] - A[n] from right to left:")
    print(array2)
    print()
    print("The third expression memorise the maximum of A[m] - A[n] + A[p] from right to left:")
    print(array3)
    print()
    print("The fourth expression memorise the maximum of A[m] - A[n] + A[p] - A[q] from right to left:")
    print(array4)
    print()
    print (f"The maximum value of the expression is situated on the first position: {array4[0]}")

A = read_sequence()
naive(A)
dynamic(A)