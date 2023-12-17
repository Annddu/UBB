# Solve the problem from the third set here
# Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,... obtained from the sequence of natural numbers
# by replacing composed numbers with their prime divisors,
# each divisor d being written d times, without memorizing the elements of the sequence.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def n_th(n):
    a = 1
    nr = 1
    i = 1
    print("The sequence is:")
    while i<=n:
        if is_prime(a) or a == 1:
            print(f"{a} ", end="")
            nr = a
            i += 1
        else:
            for j in range(2, int (a/2 +1)):
                if a % j == 0 and is_prime(j):
                    cnt = j
                    nr = j
                    while cnt != 0 and i<=n:
                        print(f"{j} ", end="")
                        cnt -= 1
                        i += 1
        a += 1
    print()    
    print(f"The {n}-th number is: {nr}")

n = int(input("Enter an number: "))
n_th(n)