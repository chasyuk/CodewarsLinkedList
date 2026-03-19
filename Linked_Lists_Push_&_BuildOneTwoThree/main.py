'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    linked_list = None
    for i in range(3, 0, -1):
        linked_list = push(linked_list, i)
    return linked_list
