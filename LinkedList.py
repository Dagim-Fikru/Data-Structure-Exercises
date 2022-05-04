

class LinkedListIterator:
    def __init__(self, __head):
        self.current = __head

    def __next__(self):
        if self.current == None:
            raise StopIteration
        Data = self.current.Data
        self.current = self.current.Next
        return Data


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def AddFirst(self, data):
        newNode = Node(data)
        if(self.__size == 0):
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            newNode.Next = self.__head
            self.__head = newNode
            self.__size += 1

    def AddLast(self, data):
        newNode = Node(data)
        if(self.__size == 0):
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            self.__tail.Next = newNode
            self.__tail = newNode
            self.__size += 1

    def __iter__(self):
        return LinkedListIterator(self.__head)

    def Get__size(self):
        return self.__size

    def RemoveFirst(self):
        self.__head = self.__head.Next

    def RemoveLast(self):
        # if self.__head == None:
        #     return None
        # if self.__head.Next == None:
        #     self.__head = None
        #     return None
        if self.__size == 0:
            return None
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
            self.__size = 0

        else:
            last = self.__head
            while(last.Next.Next):
                last = last.Next
            self.__tail = last
            last.Next = None
            self.__size -= 1

    def RemoveAtIndex(self, index):
        if index == 0:
            return self.RemoveFirst()
        elif index >= self.__size:
            return self.RemoveLast()
        else:
            element = self.__head
            for i in range(1, index):
                element = element.Next
            # temp = element.Next
            # element.Next = Node(data)
            element.Next = element.Next.Next
            self.__size -= 1

    def Insert(self, index, data):
        if index == 0:
            return self.AddFirst(data)
        elif index >= self.__size:
            return self.AddLast(data)
        else:
            element = self.__head
            for i in range(1, index):
                element = element.Next
            temp = element.Next
            element.Next = Node(data)
            element.Next.Next = temp
            self.__size += 1

    def All(self):
        curr = self.__head
        while(curr != None):
            print(curr.Data)
            curr = curr.Next

    def IsEmpty(self):
        return self.__size == 0

    def GetFirst(self):
        return self.__head

    def GetLast(self):
        return self.__tail


def main():
    myList = LinkedList()
    myList.AddFirst(2)
    myList.AddFirst(6)
    myList.AddFirst(10)
    myList.AddFirst(11)
    for data in myList:
        print(data, end=" ")
    myList.Insert(1, 12)
    for data in myList:
        print(data, end=" ")
    print(myList.RemoveAtIndex(2))
    for data in myList:
        print(data, end=" ")

    # myList.RemoveLast()
    # print(myList.__size)
    # print(myList.GetFirst().Data)
    # myList.RemoveLast()
    # myList.RemoveLast()
    # myList.RemoveLast()
    # print(myList.IsEmpty())
    # print(myList.GetLast().Data)
    # print(myList.GetLast().Data)


if __name__ == '__main__':
    main()