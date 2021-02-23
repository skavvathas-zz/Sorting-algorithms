# Merge sort in a list (array)
def merge_sort(low, high, array):

    if len(array) > 1:
        middle = int((low+high)/2)
        
        if low < middle:
            merge_sort(low, middle, array)
        if high > middle+1:
            merge_sort(middle+1, high, array)

        for j in range(middle+1, high+1, 1):
            for i in range(low, j, 1):
                if array[j] < array[i]:
                    p = array[j]
                    for k in range(j, i, -1):
                        array[k] = array[k-1]
                    array[i] = p
                    j += 1
                    break
                else:   # array[j] > array[i]
                    i += 1


