from dlist import *

# swap 2 nodes
def swap_nodes(node1, node2):
    swap = Node(0)

    # swap points where node1 points
    swap.next = node1.next
    swap.prev = node1.prev
    if node1.next is not None:
        node1.next.prev = swap
    node1.prev.next = swap

    # node1 goes to node2 position
    node1.next = node2.next
    node1.prev = node2.prev
    if node2.next is not None:
        node2.next.prev = node1
    node2.prev.next = node1

    # node2 goes to node1 position
    node2.next = swap.next
    node2.prev = swap.prev
    if swap.next is not None:
        swap.next.prev = node2
    swap.prev.next = node2

def swap_head(list, node1, node2):
    swap = Node(0)

    # swap points where node2 points
    swap.next = node2.next
    swap.prev = node2.prev
    if node2.next is not None:
        node2.next.prev = swap
    node2.prev.next = swap

    # node2 goes to node1 position
    list.head = node2
    node2.next = node1.next
    node2.prev = None
    if node1.next.prev is not None:
        node1.next.prev = node2
    
    # node2 goes to node1 position
    node1.next = swap.next
    node1.prev = swap.prev
    if swap.next is not None:
        swap.next.prev = node1
    swap.prev.next = node1

