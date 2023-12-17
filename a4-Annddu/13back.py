#    Backtraking
#13. The sequence a1, ..., an of distinct integer numbers is given. Display all subsets with a mountain aspect.
#    A set has a mountain aspect if the elements increase up to a point and then they decrease. E.g. 10, 16, 27, 18, 14, 7.

def read_sequence ():
    string = input("Enter an list: ")
    import re
    return [int(s) for s in re.findall(r"-?\d+", string)]
    
def validMountain(mountain, n):
    left = 0
    right = n - 1
    while left < n - 1 and mountain[left] < mountain[left +1]:
        left = left + 1
    while right > 0 and mountain[right - 1] > mountain[right]:
        right = right - 1
    if left > 0 and left == right and right < n - 1:
        return True
    else:
        return False

def verif(k,subset):
    for q in range (0, k):
        if subset[k] == subset [q]:
            return False
        
    peak_index = 0
    for i in range(1, k):
        if subset[i] > subset[i - 1]:
            peak_index = i
        else:
            break
    
    for i in range(peak_index + 1, k):
        if not subset[i] < subset[i - 1]:
            return False
    
    return True

def back(k, n, p, arr, subset):
    for j in range (0, n):
        subset[k] = arr[j]
        if verif(k,subset) is True:
            if k + 1 == p: 
                if validMountain(subset,len(subset)):
                    print(subset)
            else:
                back(k + 1, n, p, arr, subset)

def iterative_back(n, p, arr):
    stack = [(0, [-1] * p)]

    while stack:
        k, subset = stack.pop()

        if k == p:
            if validMountain(subset, len(subset)):
                print(subset)
        else:
            for j in range(n):
                subset[k] = arr[j]
                if verif(k, subset):
                    stack.append((k + 1, subset[:]))
                  
#arr = [2, 5, 65, 6, 54, 76, -10, -100, 100, 0]
subset = [0]
arr = read_sequence()

print("Backtraking recursiv")
import time
start = time.time()
for i in range(3, len(arr)+1):
    subset = subset*(i)
    back(0, len(arr), i, arr, subset)
    subset = [0]
end = time.time()

print("Backtraking iterativ")
start1 = time.time()
for i in range(3, len(arr)+1):
    iterative_back(len(arr),i,arr)
end1 = time.time()

print(f"{len(arr)} numbers:")
print(f"Backtraking recursiv: {end - start} seconds")
print(f"Backtraking iterativ: {end1 - start1} seconds")