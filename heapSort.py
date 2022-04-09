
# class Heap:
#     def __init__(self):
#         self.Nodes = []

#     def add(self,item):
#         self.Nodes.append(item)
#         current = len(self.Nodes) -1
#         parent = (current -1)//2
#         while self.Nodes[current] > self.Nodes[parent]:
#             self.Nodes[current] , self.Nodes[parent] = self.Nodes[parent] , self.Nodes[current]
#             current = parent
#             parent = (current-1)//2

#     def getList(self):
#         return self.Nodes

#     def Peek(self):
#         return self.Nodes[0]

#     def isEmpty(self):
#         return len(self.Nodes)==0 

#     def getSize(self):
#         return len(self.Nodes)

# def main():
#     myHeap =  Heap()

#     list = [3,1,5,4,7,0]
#     for i in range (len(list) - 1):
#         myHeap.add(list[i])
#     print(myHeap.getList)

# main

from Heap import Heap

def heapSort(list):
    heap = Heap()

    for v in list:
        heap.add(v)

    for i in range (len(list)):
        list[len(list)-1-i] = heap.remove()

def main():
    list = [50,2,1,7]
    heapSort(list)
    for v in list:
        print(str(v) + " ",end= " ")

main()

        