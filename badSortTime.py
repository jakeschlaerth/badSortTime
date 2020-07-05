# Author: Jacob Schlaerth
# Date: 07/05/2020

import math
import random
import time

while True:  # driver code for alpha user input
    try:
        alpha = float(input("Please input desired alpha parameter such that 0 < alpha < 1 :  "))
    except ValueError:
        print("invalid input. Please enter a decimal value between 0 and 1")
        continue
    if alpha < 0 or alpha > 1:
        print("invalid input. Please enter a decimal value between 0 and 1")
        continue
    if alpha <= .5:
        print("warning: this alpha parameter will not correctly sort data.")
        break
    break


def randList(n):
    """
    fills an list of length n with random integers between 0 and 10000
    :param n: length of list
    :return: list
    """
    rand_list = []
    for i in range(0, n):
        rand_list.append(random.randint(0, 10000))
    return rand_list


def badSort(arr, left, right):
    n = right - left + 1
    if left + 1 == right:  # if the length of the sub-array being checked is 2
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

    if n > 2:  # if the length of the sub-array is > 2
        m = math.ceil(n * alpha)

        if m == n and n > 2:  # if m == n and n is > 2, n will never decrease and we will recurse infinitely
            m -= 1

        badSort(arr, left, (left + m - 1))
        badSort(arr, (right - m + 1), right)
        badSort(arr, left, (left + m - 1))

# driver code for random arrays
for i in range(100, 1000, 100):
    random_list = randList(i)
    print("array of length", i, "sorted in ", end="")
    start_time = time.perf_counter()
    badSort(random_list, 0, i-1)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(run_time, end="")
    print(" seconds via badSort with an alpha parameter of ", end="")
    print(alpha)

