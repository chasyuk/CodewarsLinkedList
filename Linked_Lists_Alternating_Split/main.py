
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception
    list_1 = Node(None)
    list_2 = Node(None)
    p1 = list_1
    p2 = list_2
    p0 = head
    while p0 is not None and p0.next is not None:
        p1.next = Node(p0.data)
        p1 = p1.next
        p2.next = Node(p0.next.data)
        p2 = p2.next
        p0 = p0.next.next
    if p0 is not None:
        p1.next = Node(p0.data)
        p1 = p1.next
    return Context(list_1.next, list_2.next)
