from preloaded import Node

def swap_pairs(head):
    if not head:
        return None
    if head.next is not None:
        temp = head
        temp_2 = head.next.next
        head = head.next
        head.next = temp
        head.next.next = temp_2
    if head.next is not None:
        p = head
        p = p.next
        while p.next is not None and p.next.next is not None:
            temp = p.next
            temp_2 = p.next.next
            temp_3 = None
            if p.next.next is not None:
                temp_3 = p.next.next.next
            p.next = temp_2
            p.next.next = temp
            p.next.next.next = temp_3
            p = p.next
            p = p.next



    return head
