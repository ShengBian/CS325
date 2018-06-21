# Author: Sheng Bian
# Date: April 8, 2017
# Description: This program implement insertion sort algorithms by
# python. It read integers from data.txt and write the result
# into insert.out file.

# The following code modified from textbook P18
def insertionSort(arr):
    for j in range(1, len(arr)):

        key = arr[j]

        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

# create insert.out file for output
with open('insert.out', 'w') as file_output:
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
            # call the insertionSort to sort the array
            insertionSort(array)
            # convert array to string and write into insert.out file
            merged = ' '.join([str(i) for i in array]) + '\n'
            file_output.write(merged)