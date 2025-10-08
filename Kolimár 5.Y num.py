import numpy as np
import time

#1
x = [1, 2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(x)
print(type(arr))
print(type(x))

#2
arr = np.array([10, 20, 30, 40, 50])
print(arr[1],arr[4])

#3
list_a = [1, 2, 3]
array_a = np.array([1, 2, 3])

print(list_a * 2)
print(array_a * 2)

# 4
list_a = [1, 2, 3]
list_b = [4, 5, 6]

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print(list_a + list_b)
print(array_a + array_b)

#5
my_list = [7, 8, 9]
my_array = np.array([10, 11, 12])
a = np.array(my_list)
b = np.array(my_array.tolist())
print(a)
print(b)

#6
nums = [1, 2, 3, 4, 5]
nums_array = np.array(nums)

print(sum(nums))
print(np.sum(nums_array))

#7
L = list(range(1_000_000))
A = np.array(L)

# List version
start = time.time()
sum_L = sum([x**2 for x in L])
print("List time:", time.time() - start)

# NumPy version
start = time.time()
sum_A = np.sum(A**2)
print("Array time:", time.time() - start)

#8
list_2d = [[1, 2], [3, 4]]
array_2d = np.array([[1, 2], [3, 4]])

print(list_2d[1][1])
print(array_2d[1, 1])