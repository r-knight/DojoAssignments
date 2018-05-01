class DLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def normalize(self):
        runner = self.head.next
        trailing = self.head
        trailing.prev = None
        while(runner.next != None):
            print (runner)
            runner.prev = trailing
            trailing = runner
            runner = runner.next
        runner.prev = trailing

    def PrintAllVals(self):
        runner = list.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print (runner.value) #print final value

    def AddBack(self,val):
        newNode = DLNode(val)
        runner = list.head
        while(runner.next != None):
            runner = runner.next
        runner.next = newNode
        newNode.prev = runner
        self.tail = newNode

    def AddFront(self,val):
        newNode = DLNode(val)
        self.head.prev = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode

    def insertBefore(self, nextVal, val):
        newNode = DLNode(val)
        if self.head.value == nextVal:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            return self
        else:
            runner = list.head
            while(runner.next !=None):
                if runner.next.value == nextVal:
                    newNode.next = runner.next
                    runner.next.prev = newNode
                    runner.next = newNode
                    return self
                runner = runner.next
        return False

    def insertAfter(self, preval, val):
        newNode = DLNode(val)
        if self.tail.value == preval:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            return self
        elif self.head.value == preval:
            self.head.next.prev = newNode
            newNode.next = self.head.next
            newNode.prev = self.head
            self.head.next = newNode
            return self
        else:
            runner = list.head
            while(runner.next !=None):
                if runner.next.value == preval:
                    runner = runner.next
                    newNode.next = runner.next
                    newNode.prev = runner
                    newNode.next.prev = newNode
                    runner.next = newNode
                    return self
                runner = runner.next
        return False
    def RemoveNode(self, val):
        if self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
            return self
        else:
            runner = list.head
            while(runner.next != None):
                if runner.next.value == val:
                    runner.next.next.prev = runner
                    runner.next = runner.next.next
                    return self
                runner = runner.next
    def ReverseList(self):
        runner = self.head
        trailing = None
        while (runner):
            trailing = runner.prev
            runner.prev = runner.next
            runner.next = trailing
            runner = runner.prev


        self.head = trailing.prev


list = DList()
list.head = DLNode('Alice')
list.head.next = DLNode('Chad')
list.head.next.prev = 'Alice'
list.head.next.next = DLNode('Debra')
list.head.next.prev = DLNode('Chad')
list.AddBack('Bob')
list.AddFront('Jim')
list.insertAfter('Jim', 'Karen')
list.insertAfter('Bob', 'Craig')
list.insertBefore('Jim', 'Eric')
list.insertBefore('Craig', 'Jeff')
list.PrintAllVals()
list.normalize()
list.ReverseList()
print("reversed?")
list.PrintAllVals()