def biggieSize(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

def countPositives(arr):
    count = 0
    for i in arr:
        if i > 0:
            count+=1
    arr[len(arr)-1] = count

def sumTotal(arr):
    sum = 0
    for item in arr:
        sum+=item
    return sum

def average(arr):
    sum = 0
    for item in arr:
        sum+=item
    return sum/len(arr)

def length(arr):
    length = 0
    for item in arr:
        length+=1
    return length

def min(arr):
    if len(arr) == 0:
        return false
    min = arr[0]
    for item in arr:
        if item < min:
            min = item
    return min
def max(arr):
    if len(arr) == 0:
        return false
    max = arr[0]
    for item in arr:
        if item > max:
            max = item
    return max
def ultimateAnalyze(arr):
    if len(arr) == 0:
        return false
    sum = 0
    max = arr[0]
    min = arr[0]
    for item in arr:
        if item < min:
            min = item
        if item > max:
            max = item
        sum+=item
    analysis = {"sum": sum, "avg": sum/len(arr), "min": min, "max": max, "length": len(arr)}
    return analysis
def reverseList(arr):
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
