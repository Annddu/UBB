# Solve the problem from the second set here
# Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n.
# Two prime numbers p and q are called twin if q - p = 2.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def twin(n):
    while True:
        if is_prime(n) and is_prime(n+2):
            print(f"The numbers are: {n} and {n+2}")
            break
        else: 
            n+=1

n = int(input("Enter an number: "))
twin(n)