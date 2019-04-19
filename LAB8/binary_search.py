def binarySearch (listNumbers, low, high, key):
    found = False
    pointer = 0
    middle = int((high + low)/2)
    if low > high:
        return -1
    if listNumbers[middle] == key:
        return middle
    if listNumbers[middle] > key:
        return binarySearch(listNumbers, low, middle-1, key)
    if listNumbers[middle] < key:
        return binarySearch(listNumbers, middle + 1, high, key)


# Test array
def main():
    array_for_test = [-8,-2,1,3,5,7,9]
    print(binarySearch(array_for_test,0,len(array_for_test)-1,9))
    print(binarySearch(array_for_test,0,len(array_for_test)-1,-8))
    print(binarySearch(array_for_test,0,len(array_for_test)-1,4))

main()
