def returnASCdictionary(min=40, max=200):
    charDict = {}
    for i in range(min, max+1):
        charDict[i] = "" + chr(i) + ""
    return charDict

def upCase(string):
    newStr = ""
    for i in range(len(string)):
        if ord(string[i])>96 and ord(string[i])<=122:
            newStr += (chr(ord(string[i])-32))
        else:
            newStr +=string[i]
    return newStr

def lowerCase(string):
    newStr = ""
    for i in range(len(string)):
        if ord(string[i])>65 and ord(string[i])<=90:
            newStr += (chr(ord(string[i])+32))
        else:
            newStr +=string[i]
    return newStr