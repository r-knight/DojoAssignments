class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def PrintAllVals(self):
        runner = list.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print (runner.value) #print final value

    def AddBack(self,val):
        newNode = SLNode(val)
        runner = list.head
        while(runner.next != None):
            runner = runner.next
        runner.next = newNode
        self.tail = newNode

    def AddFront(self,val):
        newNode = SLNode(val)
        newNode.next = self.head
        self.head = newNode

    def insertBefore(self, nextVal, val):
        newNode = SLNode(val)
        if self.head.value == nextVal:
            newNode.next = self.head
            self.head = newNode
            return self
        else:
            runner = list.head
            while(runner.next !=None):
                if runner.next.value == nextVal:
                    newNode.next = runner.next
                    runner.next = newNode
                    return self
                runner = runner.next
        return False
    def insertAfter(self, preval, val):
        newNode = SLNode(val)
        if self.tail.value == preval:
            self.tail.next = newNode
            self.tail = newNode
            return self
        elif self.head.value == preval:
            newNode.next = self.head.next
            self.head.next = newNode
            return self
        else:
            runner = list.head
            while(runner.next !=None):
                if runner.next.value == preval:
                    runner = runner.next
                    newNode.next = runner.next
                    runner.next = newNode
                    return self
                runner = runner.next
        return False
    def RemoveNode(self, val):
        if self.head.value == val:
            self.head = self.head.next
            return self
        else:
            runner = list.head
            while(runner.next != None):
                if runner.next.value == val:
                    runner.next = runner.next.next
                    return self
                runner = runner.next
    def ReverseList(self):
        runner = self.head
        trailing = None
        while (runner):
            nextNode = runner.next #store runner's next node
            runner.next = trailing 
            trailing = runner #reverse trailing's pointer
            runner = nextNode #continue to next node

        self.head = trailing #reset head pointer to new head pointer


list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')
list.AddBack('Bob')
list.AddFront('Jim')
list.insertAfter('Jim', 'Karen')
list.insertAfter('Bob', 'Craig')
list.insertBefore('Jim', 'Eric')
list.insertBefore('Craig', 'Jeff')
list.PrintAllVals()
list.ReverseList()
print("reversed?")
list.PrintAllVals()