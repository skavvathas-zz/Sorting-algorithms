# Quick sort in a list (array)
def quick_sort(low, high, array):
   
    i = low
    j = high-1
    pivot = array[high]

    while i <= j:
        if array[i] > pivot and array[j] < pivot:
            array[i], array[j] = array[j], array[i]
        elif array[i] > pivot and array[j] > pivot:
            j -= 1
        elif array[i] < pivot and array[j] < pivot:
            i += 1
        else:
            i += 1
            j -= 1

    array[high], array[i] = array[i], array[high]

    if low <= i-1:
        quick_sort(low, i-1, array)
    if i+1 <= high:
        quick_sort(i+1, high, array)

