#24.	Write a program to Reverse the Linked List. Input: 1->2->3->4->5->NULL Output: 5->4->3->2->1->NULL

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

def printLL(start: Node):
    pointer = start
    while pointer != None:
        print(pointer.value, end ="->")
        pointer = pointer.next
    else:
        print("Null")

def reverseLL(start: Node) -> Node:
    if start == None or start.next == None:
        return start

    first = start
    second = first.next
    first.next = None

    while second != None:
        third = second.next
        second.next = first
        first = second
        second = third

    return first


if __name__ == "__main__":
    printLL(l1)
    reverseLL(l1)
    printLL(l5)