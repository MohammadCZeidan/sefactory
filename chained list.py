# Each Node stores data and a reference to the next node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# The LinkedList class manages the nodes
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_value(self, value):
        if not self.head:
            print("List is empty.")
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

        print(f"Value {value} not found in list.")

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    # (Optional)
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


linked_list = LinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)

linked_list.display()  # Output: 5 -> 10 -> 20 -> None

linked_list.delete_value(10)
linked_list.display()  # Output: 5 -> 20 -> None

print(linked_list.search(20))  # True
print(linked_list.search(50))  # False

print("Length:", linked_list.length())  # 2
