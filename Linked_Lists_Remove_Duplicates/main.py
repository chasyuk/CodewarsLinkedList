class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return None
    p1 = head
    list_2 = Node(p1.data)
    if p1.next:
        p2 = list_2
        while p1.next is not None:
            if p1.data != p1.next.data:
                p2.next = Node(p1.next.data)
                p2 = p2.next
            p1 = p1.next
    return list_2
