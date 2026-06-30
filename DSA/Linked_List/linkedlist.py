from typing import Optional, Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    # Insert at beginning
    def insert_begin(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Insert at a given position (0-based indexing)
    def insert_at_position(self, pos: int, data: Any) -> None:
        if pos < 0:
            print("Invalid Position")
            return

        if pos == 0:
            self.insert_begin(data)
            return

        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_begin(self) -> None:
        if self.head is not None:
            self.head = self.head.next

    # Delete from end
    def delete_end(self) -> None:
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next is not None and temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # Delete by value
    def delete_value(self, value: Any) -> None:
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None and temp.next.data != value:
            temp = temp.next

        if temp.next is not None:
            temp.next = temp.next.next

    # Search
    def search(self, value: Any) -> int:
        temp = self.head
        pos = 0

        while temp is not None:
            if temp.data == value:
                return pos
            temp = temp.next
            pos += 1

        return -1

    # Count nodes
    def count(self) -> int:
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    # Reverse linked list
    def reverse(self) -> None:
        prev: Optional[Node] = None
        curr = self.head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    # Display
    def display(self) -> None:
        if self.head is None:
            print("Linked List is Empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# ---------------- DRIVER CODE ----------------

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print("Initial List:")
ll.display()

ll.insert_begin(5)
print("\nAfter Insert at Beginning:")
ll.display()

ll.insert_end(40)
print("\nAfter Insert at End:")
ll.display()

ll.insert_at_position(2, 15)
print("\nAfter Insert at Position 2:")
ll.display()

print("\nCount:", ll.count())
print("Search 20:", ll.search(20))

ll.delete_begin()
print("\nAfter Delete Beginning:")
ll.display()

ll.delete_end()
print("\nAfter Delete End:")
ll.display()

ll.delete_value(20)
print("\nAfter Delete Value 20:")
ll.display()

ll.reverse()
print("\nAfter Reverse:")
ll.display()