""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if not head:
        head = Node(data)
        return head

    p1 = head
    if data < p1.data:
        head = Node(data)
        head.next = p1

    else:
        while p1.next is not None:
            if data < p1.next.data:
                temp = p1.next
                p1.next = Node(data)
                p1.next.next = temp
                break
            p1 = p1.next
        else:
            p1.next = Node(data)
    return head
