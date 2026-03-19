def linked_list_from_string(list_repr: str) -> Node | None:
    list_repr = list_repr.split(' -> ')
    list_repr = [int(el) for el in list_repr if el != 'None']
    linked_list = None
    if list_repr:
        linked_list = Node(list_repr[0])
        p = linked_list
        for el in list_repr[1:]:
            if el != None:
                p.next = Node(el)
                p = p.next

    return linked_list
