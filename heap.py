
class Heap:
    def __init__(self):
        self.Nodes = []

    def add(self , e):
        self.Nodes.append(e)
        current = len(self.Nodes) -1 

        while current>0:
            parent = (current - 1)//2
            if self.Nodes[current] > self.Nodes[parent]:
                self.Nodes[current] , self.Nodes[parent] = self.Nodes[parent] , self.Nodes[current]
            else:
                break
            current = parent

    def remove(self):

        if len(self.Nodes) == 0:
            return None

        removedItem = self.Nodes[0]
        self.Nodes[0] = self.Nodes[len(self.Nodes) -1]
        self.Nodes.pop(len(self.Nodes) -1)
        current = 0
        while current < len(self.Nodes):
            leftIndex = 2* current + 1
            rightIndex = 2* current + 2

            if leftIndex >= len(self.Nodes):
                break
            maxIndex = leftIndex

            if rightIndex <len(self.Nodes):
                if self.Nodes[maxIndex]< self.Nodes[rightIndex]:
                    maxIndex = rightIndex
                if self.Nodes[current] < self.Nodes[maxIndex]:
                    self.Nodes[maxIndex] , self.Nodes[current]= self.Nodes[current] , self.Nodes[maxIndex]
                    current = maxIndex
                else:
                    break
            return removedItem

    def getSize(self):
        return len(self.Nodes)

    def isEmpty(self):
        return self.getSize() == 0

    def peek(self):
        return self.Nodes[0]

    def getList(self):
        return self.Nodes

        