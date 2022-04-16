def mergeTwoSortedLists(listA,listB):
    sortedList = []
    a = len(listA)
    b = len(listB)
    i=j=0
    while i < a and j < b:
        if listA[i]<=listB[j]:
            sortedList.append(listA[i])
            i+=1

        else:
            sortedList.append(listB[j])
            j+=1

    while i<a:
        sortedList.append(listA[i])
        i+=1
    while j<b:
        sortedList.append(listB[j])
        j+=1

    return sortedList


def main():
    listA = [1,2,3,40,50,100]
    listB = [20,25,55,95,100,120]

    print(mergeTwoSortedLists(listA,listB))
main()
