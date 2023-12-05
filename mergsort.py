# -*- coding: utf-8 -*-
"""MergSort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bsQSTl4x92OiOH-aU2XkrfgUtnORRXpm
"""

import time
from random import *
import matplotlib.pyplot as plt
import pandas as pd
import random

def merge(a, beg, mid, end):
    n1 = mid - beg + 1
    n2 = end - mid

    LeftArray = [0] * n1
    RightArray = [0] * n2

    # Copy data to temporary arrays
    for i in range(n1):
        LeftArray[i] = a[beg + i]

    for j in range(n2):
        RightArray[j] = a[mid + 1 + j]

    i = 0  # Initial index of first sub-array
    j = 0  # Initial index of second sub-array
    k = beg  # Initial index of merged sub-array

    while i < n1 and j < n2:
        if LeftArray[i] <= RightArray[j]:
            a[k] = LeftArray[i]
            i += 1
        else:
            a[k] = RightArray[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = LeftArray[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = RightArray[j]
        j += 1
        k += 1


def mergeSort(a, beg, end):
    if beg < end:
        mid = (beg + end) // 2
        mergeSort(a, beg, mid)
        mergeSort(a, mid + 1, end)
        merge(a, beg, mid, end)

size = 1000
size1 = 5000
size2 = 10000

beg = 1
end = size
end1 = size1
end2 = size2

best = list(range(1, size+1))
worst = list(range(size+1, 1, -1))
avg = list(range(1, size+1))
random.shuffle(avg)

best1 = list(range(1, size1+1))
worst1 = list(range(size1+1, 1, -1))
avg1 = list(range(1, size1+1))
random.shuffle(avg1)

best2 = list(range(1, size2+1))
worst2 = list(range(size2+1, 1, -1))
avg2 = list(range(1, size2+1))
random.shuffle(avg2)

num_iterations = 100

total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(best, 0, size-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time = total_time / num_iterations

print("Average time for best case with size = 1000: {:.6f} seconds".format(average_time))


total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(best1, 0, size1-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time0 = total_time / num_iterations

print("Average time for best case with size = 5000: {:.6f} seconds".format(average_time0))


total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(best2, 0, size2-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time00 = total_time / num_iterations

print("Average time for best case with size = 10000: {:.6f} seconds".format(average_time00))

num_iterations = 100
total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(worst, 0, size-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time1 = total_time / num_iterations

print("Average time for worst case with size = 1000: {:.6f} seconds".format(average_time1))


total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(worst1, 0, size1-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time11 = total_time / num_iterations

print("Average time for worst case with size = 5000: {:.6f} seconds".format(average_time11))


total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(worst2, 0, size2-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time111 = total_time / num_iterations

print("Average time for worst case with size = 10000: {:.6f} seconds".format(average_time111))

num_iterations = 100

total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(avg, 0, size-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time2 = total_time / num_iterations

print("Average time for avg case with size = 1000: {:.6f} seconds".format(average_time2))


total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(avg1, 0, size1-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time22 = total_time / num_iterations

print("Average time for avg case with size = 5000: {:.6f} seconds".format(average_time22))

total_time = 0

for _ in range(num_iterations):
    start_time = time.time()

    sorted_avg = mergeSort(avg2, 0, size2-1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

average_time222 = total_time / num_iterations

print("Average time for avg case with size = 10000: {:.6f} seconds".format(average_time222))

# initialize data of lists.
# n: represents the input size
# case: whether it is best, average or worst
# time: the average running time for each case and input
data = {'n': [1000, 1000, 1000, 5000, 5000, 5000, 10000, 10000, 10000],
        'case': ['best',  'worst', 'average', 'best',  'worst', 'average', 'best',  'worst', 'average'],
        'time': [average_time, average_time1, average_time2, average_time0, average_time11, average_time22, average_time00, average_time111, average_time222]}


# Creates pandas DataFrame.
df = pd.DataFrame(data)


# print the data
df


#import plotly to chart your data
import plotly.express as px

# data is taken from the above data frame, x axis is coming from the input size,
# y axis is coming from time, and color of each line is based on the case
fig = px.line(data, x='n', y='time', color='case')


# make sure the x axis is categorical so it is not charted according to its value
fig.update_layout(xaxis_type='category')

# indicate the type of the line and show the chart
fig.update_traces(mode='markers+lines')
fig.show()