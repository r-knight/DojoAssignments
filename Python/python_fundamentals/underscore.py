    def map(list, function):
        for i in range(len(list)):
            list[i] = function(list[i])
        return list
    def reduce(list, function, memo):
        # your code here
        for i in range(len(list)):
            memo+= function(list[i])
        return memo
    def find(list, function):
        # your code here
        for i in list:
            if function(i) == True:
                return i
    def filter(list, function):
        # your code 
        filtered = []
        for i in list:
            if function(i) == True:
                filtered.append(i)
        return filtered
    def reject(list, function):
        # your code
        rejected = []
        for i in list:
            if function(i) != True:
                rejected.append(i)
        return rejected
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above