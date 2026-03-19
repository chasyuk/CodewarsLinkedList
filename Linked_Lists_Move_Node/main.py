class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if not dest:
        dest = Node(source.data)
        source = source.next
        return Context(source, dest)
    if not source:
        raise Exception
    new_node = Node(source.data)
    new_node.next = dest
    source = source.next
    return Context(source, new_node)
