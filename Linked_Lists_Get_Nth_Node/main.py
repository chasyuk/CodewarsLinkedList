# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if not node:
        raise ValueError
    if not isinstance(index, int) or index < 0:
        raise IndexError
    i = 0
    p = node
    while i < index:
        i += 1
        p = p.next
        if p is None:
            raise IndexError
    return p
