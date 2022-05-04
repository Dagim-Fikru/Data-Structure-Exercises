from stack import Stack
class Queue:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = [] 

    def enQueue(self, data):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(data)

        while len(self.stack2) != 0:
            # self.stack1.append(self.stack2[-1])
            self.stack2.pop(self.stack2[-1])

    def deQueue(self):

        if len(self.stack1) == 0:
            print("Q is Empty")

        data = self.stack1[-1]
        self.stack1.pop()
        return data

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())