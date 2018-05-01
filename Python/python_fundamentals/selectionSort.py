def selectionSort(unsorted):
    for i in range(len(unsorted)):
        tempMin = i
        for j in range(i+1, len(unsorted)):
            if unsorted[j] < unsorted[tempMin]:
                tempMin = j
        if tempMin != i:
            temp = unsorted[i]
            unsorted[i] = unsorted[tempMin]
            unsorted[tempMin] = temp
    return unsorted

