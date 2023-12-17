#cocktail 
#hip sort
#hip sort
#copy.deepcopy(l)

def menu():
    print("")
    print("1. Generate a random list of n numbers")
    print("2. Use cocktail sort")
    print("3. Use hip sort")
    print("4. Exit the program")
    print("")

def generate_list(n: int):
    import random
    rand_list=[]
    for i in range(n):
        rand_list.append(random.randint(0,100))
    print("The list is:")
    print(rand_list)
    print("")
    return rand_list

def cocktail_sort(array, len, steps):
    swap = True
    start = 0 #first
    end = len - 1 #last
    cnt = 0
    while (swap == True):
        swap = False
        for a in range(start, end):
            if (array[a] > array[a+1]):
                array[a], array[a+1] = array[a+1], array[a]
                cnt += 1
                if cnt == steps:
                    print(array)
                    cnt = 0
                swap = True
        if(swap == False):
            end = end-1
        for a in range(end-1, start-1, -1):
            if(array[a] > array[a+1]):
                array[a], array[a+1] = array[a+1], array[a]
                cnt += 1
                if cnt == steps:
                    print(array)
                    cnt = 0
                swap = True
        start = start+1
    print(array)

def heapify(arr, n, i, steps, cnt):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        cnt += 1
        if cnt == steps:
            print(arr)
            cnt = 0
        heapify(arr, n, largest, steps, cnt)


def heapSort(arr, steps):
    n = len(arr)
    cnt = 0

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i, steps, cnt)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        cnt += 1
        if cnt == steps:
            print(arr)
            cnt = 0

        # Heapify root element
        heapify(arr, i, 0, steps, cnt)
    print(arr)

def main():
    rand_list = []
    aux_rand_list = []

    while True:
        menu()
        option = input("Enter an number: ")
        print("")

        if option == "1":
            import copy
            n = int(input("Enter the number of elements in the list: "))
            rand_list = generate_list(n)
            aux_rand_lis = copy.deepcopy(rand_list)

        elif option == "2":
            import copy
            if rand_list:
                steps = int((input("Enter the number of steps: ")))
                cocktail_sort(rand_list, len(rand_list), steps)
                rand_list= copy.deepcopy(aux_rand_lis)
            else: 
                print("Please first generate a list")

        elif option == "3":
            import copy
            if rand_list:
                steps = int((input("Enter the number of steps: ")))
                heapSort(rand_list, steps)
                rand_list= copy.deepcopy(aux_rand_lis)
            else: 
                print("Please first generate a list")

        elif option == "4":
            break

        else: 
            print("Please enter number from the menu!")

main()