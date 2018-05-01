def insertionSort(unsorted):
    for i in range(1, len(unsorted)):
        j = i
        while j-1 >= 0 and unsorted[j] < unsorted[j-1]:
            temp = unsorted[j]
            unsorted[j] = unsorted[j-1]
            unsorted[j-1] = temp
            j -=1
    return unsorted