class Stack:
    def __init__(self):
        self.__elements = []
    def isEmpty(self):
        return len(self.__elements)==0

    def peek(self):
        return self.__elements[-1]

    def push(self,data):
        self.__elements.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        return self.__elements.pop()

    def getSize(self):
        return len(self.__elements)

def main():
    myStack = Stack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(25)
    myStack.push(30)
    
    while (myStack.getSize()>0):
        print(myStack.pop() , end=' ')
main()