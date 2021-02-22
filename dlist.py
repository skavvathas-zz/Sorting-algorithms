class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class Double_list:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            new_node.next = None
            new_node.prev = self.head
        else:
            last = Node(data)
            last = self.head

            while(last.next is not None):
                last = last.next

            last.next = new_node
            new_node.prev = last
            new_node.next = None
            

    def list_print(self):
        new_node = self.head
        if(new_node is None):
            print("The list is empty")
            return

        print("The list is: ")

        while(new_node is not None):
            print(new_node.data)
            new_node = new_node.next

