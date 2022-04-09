
def partition(start, end, list):
     
    # Initializing pivot's index to start
    pivot_index = start
    pivot = list[pivot_index]
     
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
         
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(list) and list[start] <= pivot:
            start += 1
             
        # Decrement the end pointer till it finds an
        # element less than pivot
        while list[end] > pivot:
            end -= 1
         
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            list[start], list[end] = list[end], list[start]
     
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    list[end], list[pivot_index] = list[pivot_index], list[end]
    
    # Returning end pointer to divide the list into 2
    return end
     
# The main function that implements QuickSort
def quick_sort(start, end, list):
     
    if (start < end):
         
        # p is partitioning index, list[p]
        # is at right place
        p = partition(start, end, list)
         
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, list)
        quick_sort(p + 1, end, list)
         
list = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(list) - 1, list)
 
print(f'Sorted list: {list}')
