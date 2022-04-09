def listToOrder(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i]= list[i] + list[i+1]
            list[i+1] = list[i] - list[i+1]
            list[i] = list[i] - list[i+1]
            listToOrder(list)
def main():
    list = [10,4,3,7,20,40,120,555,-50]
    print(list)
    listToOrder(list)
    print(list)
main()
