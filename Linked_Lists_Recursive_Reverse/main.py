class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    new_list = Node()
    p2 = new_list
    p1 = head
    if head is None:
        return None
    def go_deeper(p1, p2):
        if p1.next is None:
            p2.next = Node(p1.data)
            return p2.next
        else:
            new_head = go_deeper(p1.next, p2)
            new_head.next = Node(p1.data)
            return new_head.next

    go_deeper(p1, p2)
    return new_list.next
