class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def add_element_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def add_a_list(self, list_of_elements):
        self.head = None
        for data in list_of_elements:
            self.add_element_at_end(data)

    def view_list(self):
        if self.head is None:
            print("The Linked List is empty")
            return

        linkedlist = ''
        itr = self.head
        while itr:
            linkedlist += str(itr.data)+'--->' if itr.next else str(itr.data)
            itr = itr.next
        print(linkedlist)

    def get_length(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next

        return counter


if __name__ == '__main__':
    list1 = LinkedList()
    list1.add_element_at_beginning(1)
    list1.add_element_at_beginning(2)
    list1.add_element_at_end(3)
    list1.add_a_list([5, 6, 7])
    print(list1.get_length())
    list1.view_list()

