def menu():
    print("")
    print("1. Generate a random list of n numbers")
    print("2. Use cocktail sort")
    print("3. Use hip sort")
    print("4. Exit the program")
    print("5. Best case")
    print("6. Average case")
    print("7. Worst case")
    print("")

def generate_list(n: int):
    import random
    rand_list=[]
    for i in range(n):
        rand_list.append(random.randint(0,100))
    return rand_list

def cocktail_sort_steps(array, len, steps):
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

def heapify_steps(arr, n, i, steps, cnt):
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
        heapify_steps(arr, n, largest, steps, cnt)

def heapSort_steps(arr, steps):
    n = len(arr)
    cnt = 0

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify_steps(arr, n, i, steps, cnt)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        cnt += 1
        if cnt == steps:
            print(arr)
            cnt = 0

        # Heapify root element
        heapify_steps(arr, i, 0, steps, cnt)
    print(arr)

def cocktail_sort(array, len):
    swap = True
    start = 0 #first
    end = len - 1 #last
    cnt = 0
    while (swap == True):
        swap = False
        for a in range(start, end):
            if (array[a] > array[a+1]):
                array[a], array[a+1] = array[a+1], array[a]
                swap = True
        if(swap == False):
            end = end-1
        for a in range(end-1, start-1, -1):
            if(array[a] > array[a+1]):
                array[a], array[a+1] = array[a+1], array[a]
                cnt += 1
                swap = True
        start = start+1

def heapify(arr, n, i):
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
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    cnt = 0

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)
    
def timer_cocktail(n, rand_list_):
    import time
    start = time.time()
    cocktail_sort(rand_list_,len(rand_list_))
    end = time.time()
    print(f"For {n} numbers it takes: {end - start} seconds")
    
def timer_heap(n, rand_list_):
    import time
    start = time.time()
    heapSort(rand_list_)
    end = time.time()
    print(f"For {n} numbers it takes: {end - start} seconds")
        
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
                cocktail_sort_steps(rand_list, len(rand_list), steps)
                rand_list= copy.deepcopy(aux_rand_lis)
            else: 
                print("Please first generate a list")

        elif option == "3":
            import copy
            if rand_list:
                steps = int((input("Enter the number of steps: ")))
                heapSort_steps(rand_list, steps)
                rand_list= copy.deepcopy(aux_rand_lis)
            else: 
                print("Please first generate a list")

        elif option == "4":
            break
            
        elif option == "5":
            print("Best case")
            print("Cocktail sort:")
            for i in range (0, 5):
                rand_list_ = generate_list(pow(2, i) * 500)
                rand_list_.sort()
                timer_cocktail(pow(2, i) * 500, rand_list_)
            print("Heap sort:")
            for i in range (0, 5):
                rand_list_ = generate_list(pow(2, i) * 8000)
                rand_list_.sort()
                timer_heap(pow(2, i) * 4000, rand_list_)
            
        elif option == "6":
            print("Avarage sort")
            print("Cocktail sort:")
            for i in range (0, 5):
                rand_list_ = generate_list(pow(2, i) * 500)
                timer_cocktail(pow(2, i) * 500, rand_list_)
            print("Heap sort:")
            for i in range (0, 5):
                rand_list_ = generate_list(pow(2, i) * 8000)
                timer_heap(pow(2, i) * 4000, rand_list_)
            
        elif option == "7":
            print("Worst case")
            print("Cocktail sort:")
            for i in range (0, 5):
                rand_list_ = generate_list(pow(2, i) * 500)
                rand_list_.sort(reverse=True)
                timer_cocktail(pow(2, i) * 500, rand_list_)
            print("Heap sort:")
            for i in range (0, 5):
                rand_list_ = generate_list(pow(2, i) * 8000)
                rand_list_.sort(reverse=True)
                timer_heap(pow(2, i) * 4000, rand_list_)
                
        else: 
            print("Please enter number from the menu!")

main()