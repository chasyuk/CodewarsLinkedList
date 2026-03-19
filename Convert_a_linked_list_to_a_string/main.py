def stringify(node):
    p = node
    output = []
    if node:
        output.append(str(p.data))
        while p.next is not None:
            output.append(str(p.next.data))
            p = p.next
    output.append('None')
    return ' -> '.join(output)
