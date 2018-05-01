def countdown(num):
    #returns an array of length num+1 when a positive number is passed as an argument
    #returns an array containing the number only if number is <-0
    arr = [num]
    for i in range(num):
        arr.append(num-1)
        num -=1
    
    return arr
def printAndReturn(first, second):
    print(first)
    return second
def firstPlusLength(list):
    return (list[0] + len(list))
def valuesGreaterThanSecond(arr):
    newArr = []
    if len(arr) == 1:
        return false
    count = 0
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            newArr.append(arr[i])
            count +=1
    
    print ("%d values greater than %d" % (count, arr[1]))
    return newArr
def thisLengthThatValue(num1, num2):
    if num1 == num2:
        print ("Jinx!")
    
    newArr = [num1]*num2
    return newArr