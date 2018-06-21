# Author: Sheng Bian
# Date: April 15, 2017
# Description: This program implement stooge sort sort algorithms by
# python. It read integers from data.txt and write the result into
# stooge.out file.

import math

# The following code modified from Homework Assignment 2
def stoogesort(arr, start, end):
    if end - start == 1 and arr[end] < arr[start]:
        arr[start], arr[end] = arr[end], arr[start]
    if end - start > 1:
        m = math.ceil((end - start + 1) * 2 / 3)
        stoogesort(arr, start, start + m - 1)
        stoogesort(arr, end - m + 1, end)
        stoogesort(arr, start, start + m - 1)

# create stooge.out file for output
with open('stooge.out', 'w') as file_output:
    # read data from data.txt
    with open('data.txt', 'r') as file_input:
        # read numbers line by line
        for line in file_input:
            # remove new line '\n'
            line = line.rstrip('\n')
            # append numbers from each line to array
            array = []
            for s in line.split(' '):
                s = int(s)
                array.append(s)
            array = array[1:]
            # call the stoogesort to sort the array
            stoogesort(array, 0, len(array) - 1)
            # convert array to string and write into stooge.out file
            merged = ' '.join([str(i) for i in array]) + '\n'
            file_output.write(merged)
