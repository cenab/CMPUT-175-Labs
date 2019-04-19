# Recursive Selection Sort Algorithm in Python 3

import random
import time

def recursive_selection_sort(array, array_len, index = 0):
    small_index = index
    if index == array_len:
        return array
    # finding smallest
    for i in range(index,array_len):
      if (array[i] > array[small_index]):
        small_index=i
    # swapping
    temp=array[index]
    array[index]=array[small_index]
    array[small_index]=temp

    index+=1
    recursive_selection_sort(array, array_len, index)

def iterative_selection_sort(data):
  for index in range(len(data)):
    small_index = index

    # finding smallest
    for i in range(index,len(data)):
      if (data[i] > data[small_index]):
        small_index=i

    # swapping
    temp=data[index]
    data[index]=data[small_index]
    data[small_index]=temp


if  __name__== "__main__":
    # Define the list of random numbers
    array_1 = [random.randint(1,1000) for i in range(200)]
    array_2 = array_1[:]
    array_len = len(array_1)
    sorted_list = sorted(array_1, reverse=True)

    # Calculate the execution time
    start_rec = time.time()
    recursive_selection_sort(array_1, array_len)
    end_rec = time.time()

    start_iter = time.time()
    iterative_selection_sort(array_2)
    end_iter = time.time()

    # Print the rsults
    print('The execution time:')
    print(' - Recursive selection sort: {}'.format(end_rec - start_rec))
    print(' - Iterative selection sort: {}'.format(end_iter - start_iter))
