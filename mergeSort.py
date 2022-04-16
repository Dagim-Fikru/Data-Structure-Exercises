def merge(list):
    a = len(list)

    #base case for the recurrision
    if a <=1:
        return list
    
    half = len(list)//2

    firstHalf = list[:half]
    secondHalf = list [half:]

    firstHalf = merge(firstHalf)
    secondHalf = merge(secondHalf)

    return mergeTwoSortedLists(firstHalf , secondHalf)




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


    test = [[50,20,22,-3,25,-22],[],[5],[1,2,3,4],[0,2,5,7]]

    for list in test:

        print(merge(list))

main()
