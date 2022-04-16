from sqlalchemy import false


def listToOrder(list):
    # for i in range(len(list)-1):
    #     if list[i] > list[i+1]:
    #         list[i]= list[i] + list[i+1]
    #         list[i+1] = list[i] - list[i+1]
    #         list[i] = list[i] - list[i+1]
    #         listToOrder(list)
    for i in range (len(list)-1):
        swap = False
        for j in range (len(list)-1-i):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                swap= True
            if not swap:
                break
def main():
    list = [10, 4, 3, 7, 20, 40, 120, 555, -50]
    print(f'before sort => {list}')
    listToOrder(list)
    print(f'after sort => {list}')
main()
