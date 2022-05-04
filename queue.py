from LinkedList import LinkedList
class Queue:
    def __init__(self):
        self.__elements = LinkedList()

    def isEmpty(self):
        return self.__elements.Isempty()

    def getSize(self):
        return self.__elements.GetSize()

    def EnQueue(self,data):
        self.__elements.AddLast(data)

    def DeQueue(self):
        return self.__elements.RemoveFirst()

def main():
    myQueue = Queue
    myQueue.EnQueue(1)
    myQueue.EnQueue(2)
    myQueue.EnQueue(3)
    myQueue.EnQueue(4)

    while (myQueue.getSize() > 0):
        print(myQueue.DeQueue() , end=' ')
main()