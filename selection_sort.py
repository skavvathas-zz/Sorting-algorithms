from dlist import *
from functions import *

#Selection sort in a doubly list
def selection_sort_1(list):
    help_node = Node(0)
    help1 = Node(0)         # with help1 node, I "run" the doubly list in every iteration
    help2 = Node(0)         # help2 has the data of the node to the right, in the right sub-table
    min_node = Node(0)

    help_node = list.head
    while help_node is not None:
        min_node = help_node
        min = min_node.data
        help1 = help_node.next
        help2 = help_node
        help_node = help_node.next
        
        while help1 is not None:
            if help1.data < min:
                min_node = help1
                min = min_node.data
                help1 = help1.next
            else:
                help1 = help1.next  

        if list.head is help2:
           swap_head(list, list.head, min_node)
        else:
            swap_nodes(help2, min_node)
        


# Selection sort in a list (array)
def selection_sort_2(arr):

    for i in range(len(arr)-1):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
