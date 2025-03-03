class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        dummy = self.head
        while index and dummy:
            dummy = dummy.next
            index -= 1
        return dummy.val if dummy else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        dummy = self.head
        while dummy.next:
            dummy = dummy.next
        dummy.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        dummy = Node(None)
        dummy.next = self.head
        current = dummy
        
        for _ in range(index):
            if current.next is None:
                return
            current = current.next
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        dummy = Node(None)
        dummy.next = self.head
        current = dummy
        for _ in range(index):
            if current.next is None:
                return 
            current = current.next
        if current.next:
            current.next = current.next.next
        self.head = dummy.next
