# Author: Sheng Bian
# Date: April 8, 2017
# Description: This program implement merge sort algorithms by
# python. It read integers from data.txt and write the result
# into merge.out file.

# The following code get reference from https://www.geeksforgeeks.org/merge-sort/
# and textbook P31 and P34
def merge(arr, p, q, r):
    # compute the length of subarray arr[p...q]
    n1 = q - p + 1
    # compute the length of subarray arr[q+1..r]
    n2 = r - q

    # create array of length n1 and n2
    L = [0] * n1
    R = [0] * n2

    # copy subarray arr[p...q] to L
    for i in range(0, n1):
        L[i] = arr[p + i]

    # copy subarray arr[q+1...r] to R
    for j in range(0, n2):
        R[j] = arr[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # copy remaining elements of L
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy remaining elements of R
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr,p,r):
    if p < r:
        q = int((p+r)/2)
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)

# create merge.out file for output
with open('merge.out', 'w') as file_output:
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
            # call the mergeSort to sort the array
            n = len(array)
            mergeSort(array, 0, n - 1)
            # convert array to string and write into merge.out file
            merged = ' '.join([str(i) for i in array])+ '\n'
            file_output.write(merged)