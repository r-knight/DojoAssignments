def basic():
    for i in range (0,151):
        print (i)

def multiplesOfFive():
    for i in range (5,1000001, 5):
        print (i)

def countingTheDojoWay():
    for i in range (1,101):
        if i%10 == 0:
            print ("Coding Dojo")
        elif i%5 == 0:
            print ("Coding")
        else:
            print(i)

def whoa():
    sum = 0
    for i in range(0,500001):
        sum +=i
    print (sum)

def countdownByFours():
    for i in range (2018,0,-4):
        print (i)

def flexibleCountdown(lowNum, highNum, mult):
    for i in range(lowNum, highNum +1):
        if i % mult == 0:
            print (i)

basic()
multiplesOfFive()
countingTheDojoWay()
whoa()
countdownByFours()
flexibleCountdown(1,9,2)