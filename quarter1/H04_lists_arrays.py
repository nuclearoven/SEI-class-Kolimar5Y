import time
import numpy as np
import random



#Exercises
def EX1():
    """
    Create a Python list and a NumPy array with the same values.
    parameters:
    -x: list
    -arr: NumPy array

    The function returns:
    -the NumPy array
    -the Python list
    -their data types
    """
    x = [1, 2, 3, 4, 5]
    arr = np.array([1, 2, 3, 4, 5])

    return arr, x,type(arr),type(x)


def EX2():
    """
    Creates a NumPy array and prints the second and last element.
    parameters:
    -arr: NumPy array

    the function returns the second and last elements of the array.
    """
    arr = np.array([10, 20, 30, 40, 50])

    return arr[1], arr[-1]


def EX3():
    """
    Demonstrate how multiplication behaves differently for lists vs arrays.
    parameters:
    -list_a: list
    -array_a: NumPy array

    results:
    -Multiplying a list repeats the list.
    -Multiplying a NumPy array multiplies each element.

    :returns the results
    """
    list_a = [1, 2, 3]
    array_a = np.array([1, 2, 3])

    return list_a* 2, array_a* 2


def EX4():
    """
    Demonstrate how addition behaves for lists vs arrays.
    parameters:
    -list_a: first list
    -list_b: second list
    -array_a: NumPy array
    -array_b: NumPy array

    the function adds the two lists together and two arrays together
    results:
    -Adding lists adds the element of both into the new list.
    -Adding NumPy arrays adds individual elements together.

    Returns combined list and array.
    """
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]

    array_a = np.array([1, 2, 3])
    array_b = np.array([4, 5, 6])

    return list_a + list_b, array_a + array_b


def EX5():
    """
    This function demonstrate converting between Python lists and NumPy arrays.
    parameters:
    -my_list: list
    -my_array: NumPy array

    Returns the NumPy array "a" converted from a list, and a list "b"
    recreated from a NumPy array.
    """
    my_list = [7, 8, 9]
    my_array = np.array([10, 11, 12])

    a = np.array(my_list)
    b = np.array(my_array.tolist())

    return a, b


def EX6():
    """
    Show the difference between summing Python lists and NumPy arrays.
    parameters:
    -nums: list
    -nums_array: NumPy array

    The function returns:
    the sum of values of the nums list
    the sum of values of the nums_array NumPy array
    """
    nums = [1, 2, 3, 4, 5]
    nums_array = np.array(nums)

    return sum(nums), np.sum(nums_array)


def EX7():
    """
    Compare performance of summing squares using a Python list vs a NumPy array.
    parameters:
    -L: list
    -A: NumPy array

    the function:
    -Creates 1,000,000 elements.
    -Measures time for list comprehension + sum().
    -Measures time for NumPy vectorized operations.
    Returns the sum of squares of the list and NumPy array.
    """
    L = list(range(1_000_000))
    A = np.array(L)

    # List version (slow)
    start = time.time()
    sum_L = sum([x ** 2 for x in L])
    print("List time:", time.time() - start)

    # NumPy version (fast due to vectorization and contiguous memory)
    start = time.time()
    sum_A = np.sum(A ** 2)
    print("Array time:", time.time() - start)

    return sum_L, sum_A


def EX8():
    """
    Demonstrate indexing in 2D lists and 2D NumPy arrays.
    parameters:
    -list_2d: 2d list
    -array_2d: 2d NumPy array

    the function returns:
    -the (1,1) element of a nested list
    -the (1,1) element of a NumPy array
    """
    list_2d = [[1, 2], [3, 4]]
    array_2d = np.array([[1, 2], [3, 4]])
    return list_2d[1][1], array_2d[1, 1]


# Execute all functions
print(EX1())
print(EX2())
print(EX3())
print(EX4())
print(EX5())
print(EX6())
EX7()
print(EX8())

#ulohy
def list(rng):
    """creates a list with random elements and the input length rng
    -it replaces the 4th element of the list with the highest value in the list
    -firstHalf: first half of the list
    -lst01: a new list consisting of random 0 and 1 and the length rng
    -lstPlus5times3: adds 5 and multiplies every element of the list by 3
    -summ: the sum of the elements of the list
    -even: even elements of the list
    -secondSmallest: second-smallest element of the list
    it then erases the list and returns the above values"""

    lst = random.sample(range(1, 100), rng)
    firstHalf = lst[:len(lst)//2]
    if len(lst) == 10:
        lst[4] = max(lst)
    print(lst[4])
    lst01 = []
    for i in range(rng):
        lst01.append(random.randint(0, 1))
    lstPlus5times3 = [(x + 5)*3 for x in lst]
    summ = sum(lst)
    even = [2 * i for i in range(1, 11)]
    secondSmallest = sorted(lst)[1]
    lst.clear()
    return firstHalf, lst01, lstPlus5times3, summ, even, secondSmallest

def array(rng):
    """creates a array with random elements and the input length rng
    -it replaces the 4th element of the list with the highest value in the array
    -firstHalf: first half of the array
    -lst01: a new array consisting of random 0 and 1 and the length rng
    -lstPlus5times3: adds 5 and multiplies every element of the array by 3
    -summ: the sum of the elements of the array
    -even: even elements of the array
    -secondSmallest: second smalest element of the array
    it then erases the array and returns the above values"""
    arr = np.random.rand(rng)
    firstHalf = arr[:rng//2]
    if arr.size == 10:
        arr[4] = arr.max()
    arr01 = np.random.randint(0,2,rng)
    arrPlus5times3 = (arr + 5)*3
    summ = np.sum(arr)
    even = np.arange(2, rng, 2)
    secondSmallest = np.sort(arr)[1]
    arr = np.delete(arr, np.arange(arr.size))
    return firstHalf, arr01, arrPlus5times3, summ, even, secondSmallest

print(list(12))
print(array(8))