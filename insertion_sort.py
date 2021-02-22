from dlist import *

# Insertion sort in a doubly list
def insertion_sort_1(list):
    compare = 0
    help_node = Node(0)
    help1 = Node(0)
    help2 = Node(0)

    help_node = list.head.next
    while(help_node is not None):
        help1 = help_node
        help_node = help_node.next
        help2 = help1.prev
        while(help2 is not None):
            if(help2 is list.head):
                if(help2.data < help1.data):
                    help2 = help2.prev
                    break
                else:
                    if(list.head.next is help1):
                        help2.next = help1.next
                        if(help1.next is not None):
                            help1.next.prev = help2
                        help2.prev = help1
                        list.head = help1
                        list.head.prev = None
                        list.head.next = help2
                        break
                    else:
                        help1.prev.next = help1.next
                        if(help1.next is not None):
                            help1.next.prev = help1.prev
                        help2.prev = help1
                        list.head = help1
                        list.head.prev = None
                        list.head.next = help2
                        break
            else:
                if(help2.data < help1.data):
                    help2 = help2.prev
                    break
                else:
                    if(help2.prev is not None):
                        compare = help2.prev.data
                    else:
                        compare = 0
                                        
                    if(help1.data < compare):
                        help2 = help2.prev
                        continue
                        
                    help1.prev.next = help1.next

                    if(help1.next is not None):
                        help1.next.prev = help1.prev
                
                    help1.next = help2
                    help1.prev = help2.prev
                    help2.prev.next = help1
                    help2.prev = help1
                    break
    

# Insertion sort in a list (array)
def insertion_sort_2(arr):

    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1

        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1

        arr[j+1] = key 
