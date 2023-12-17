# 2
# Write the implementation for A5 in this file
#
import random
import re
import math

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
# def get_real(complex_number):
#     """
#      Real part of the list
#      :complex_number: the complex number
#      :return: the value of the real part
#      """
#     return complex_number[0]

# def get_imaginary(complex_number):
#     """
#      Imaginary part of the dic.
#      :complex_number: the complex number
#      :return: the value of the imaginary part
#      """
#     return complex_number[1]

# def create_complex_number(real_part: float, imaginary_part: float):
#     """
#      Create the complex number
#      :real_part: the reall part
#      :imaginary_part: the imaginary part
#      :return: the complex number
#      """
#     complex_number = [real_part, imaginary_part]
#     return complex_number
  
#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def get_real(complex_number):
    """
    Real part of the dic.
    :complex_number: the complex number
    :return: the value of the real part
    """
    return complex_number["real part"]

def get_imaginary(complex_number):
    """
    Imaginary part of the dic.
    :complex_number: the complex number
    :return: the value of the imaginary part
    """
    return complex_number["imaginary part"]

def create_complex_number(real_part: float, imaginary_part: float):
    """
    Create the complex number
    :real_part: the reall part
    :imaginary_part: the imaginary part
    :return: the complex number
    """
    complex_number = {"real part": real_part, "imaginary part": imaginary_part}
    return complex_number

#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def to_str(complex_number):
    """
    Transforms a complex number in to a string
    :complex_number: the complex number that is going to be transformed
    :return: the string containing the complex number
    """
    if get_imaginary(complex_number) >= 0:
        return f"{get_real(complex_number)}+{get_imaginary(complex_number)}i"
    else:
        return f"{get_real(complex_number)}{get_imaginary(complex_number)}i"

def add_complex_number_to_list(complex_number_list, complex_number):
    """
    Adds a complex numbers to the list
    :complex_number_list: the list of complex numbers
    :complex_number: the complex number that is going to be added in the list
    """
    complex_number_list.append(complex_number)

def generate_complex_list(n: int) -> list:
    """
    Generate a list of n complex numbers with 'random' values
    :param n: the numbers of complec numbers to be generated
    :return: the list containing the generated complex numbers
            len(list) = n
    """
    complex_list = []
    for i in range(n):
        real_part = random.randint(-10, 10)
        imaginary_part = random.randint(-10, 10)

        complex_number = create_complex_number(real_part, imaginary_part)
        add_complex_number_to_list(complex_list,complex_number)
    return complex_list

def modulus_complex(real_part, imaginary_part):
    """
    Calculate the value of the modulus of a complex number
    :param real_par: the real part of the number
    :imaginary_part: the imaginary part of the number
    :return: the value of the modulus of a complex number
    """
    return math.sqrt(real_part**2 + imaginary_part**2)

def five_naive(complex_list):
    """
    Length and elements of a longest subarray of numbers where each number's modulus is in the [0, 10] range.
    :complex_list: the complex list
    :return: the first and last index of the subarray
    """
    first = 0
    last = -2
    for i, complex_number in enumerate(complex_list):
        for j, complex_number in enumerate(complex_list):
            ok = True
            for k, complex_number in enumerate(complex_list):
                if (j >= i) and i <= k <= j and not 0 <= modulus_complex(get_real(complex_number), get_imaginary(complex_number)) <= 10:
                    ok = False
            if ok and j - i + 1 > last - first + 1:
                first = i
                last = j
    return first,last       

def twelve_dynamic(complex_list:list):
    """
    The length and elements of a longest alternating subsequence, when considering each number's real part")
    :complex_list: the complex list
    :return: the maximum value and the list of the alternating subsequence
    """
    length = len(complex_list)
    dp = [[1, 1] for _ in range(length)]
    for i in range(length):
        real_part_i = int(get_real(complex_list[i]))
        for j in range(i):
            real_part_j = int(get_real(complex_list[j]))
            # peak up
            if real_part_i > real_part_j and dp[i][0] < dp[j][1] + 1:
                dp[i][0] = dp[j][1] + 1
            # peak down
            elif real_part_i < real_part_j and dp[i][1] < dp[j][0] + 1:
                dp[i][1] = dp[j][0] + 1
    # We search max length of sub
    max_length = max(max(dp))
    result = []
    for i in range(length - 1, -1, -1):
        if max(dp[i]) == max_length:
            result.append(complex_list[i])
            max_length -= 1
    max_length = max(max(dp))
    result.reverse()
    return result, max_length

#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def print_menu():
    """
    Print menu
    """
    print()
    print("1. Add complex numbers (blank space to stop)")
    print("2. Display the complex numbers")
    print("3. Length and elements of a longest subarray of numbers where each number's modulus is in the [0, 10] range.\n   The length and elements of a longest alternating subsequence, when considering each number's real part")
    print("4. Exit")
    print()

def show_complex_numbers(complex_number_list):
    """
    Print the list of complex numbers
    :complex_list: the complex list
    """
    for complex_number_index, complex_number in enumerate(complex_number_list):
        print('Complex number #' + str(complex_number_index + 1) + ':', to_str(complex_number))

def print_five_naive(complex_list):
    """
    Print the list of complex numbers for the naive problem
    :complex_list: the complex list
    """
    first, last = five_naive(complex_list)
    print("Length and elements of a longest subarray of numbers where each number's modulus is in the [0, 10] range.")
    print("Maximum lenght is: ", last - first + 1)
    for complex_number_index, complex_number in enumerate(complex_list):
        if first <= complex_number_index <= last:
            print('Complex number #' + str(complex_number_index + 1), to_str(complex_number)," modulus = ", modulus_complex(get_real(complex_number), get_imaginary(complex_number)))
    print()

def print_twelve_dynamic(complex_list):
    """
    Print the list of complex numbers for the dynamic problem
    :complex_list: the complex list
    """
    subsequence, lenght = twelve_dynamic(complex_list)
    print("The leght of the longest subsequence is: ", lenght,"\n", "The subsequence: ")
    for complex_number_index, complex_number in enumerate(subsequence):
        print('Complex number #' + str(complex_list.index(complex_number) + 1) + ':', to_str(complex_number))

def read_complex_numbers(complex_list):
    """
    Reads the necessary data for creating an imaginary number from the user
    """
    string = ' '
    complex_pattern = re.compile(r'^([+-]?\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?([+-]\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?i$')
    while True:
        string = input("Enter a complex number: ")
        try:
            if string == '':
                break
            else:
                if complex_pattern.match(string):
                    numbers = [int(s) for s in re.findall(r"-?\d+", string)]
                    complex_number = create_complex_number(numbers[0], numbers[1])
                    add_complex_number_to_list(complex_list, complex_number)
                else:
                    print("Please enter a viable form of a complex number")
        except IndexError:
            print("Please enter a viable form of a complex number")

def main():
    """
    Main function
    """
    complex_list = generate_complex_list(10)
    while True:
        print_menu()
        option = input("Please choose one of these options: ")
        print()
        while not option.isnumeric() or not int(option) in [1, 2, 3, 4]:
            option = input("Please enter a valid value: ")
        option = int(option)
        if option == 1:
            read_complex_numbers(complex_list)         
        if option == 2:
            show_complex_numbers(complex_list)
        if option == 3:
            print_five_naive(complex_list)
            print_twelve_dynamic(complex_list)
        if option == 4:
            print("Exiting...")
            break
        
main()