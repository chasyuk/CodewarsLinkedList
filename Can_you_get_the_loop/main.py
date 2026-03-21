def loop_size(node):
    fast = node
    slow = node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            slow = slow.next
            loop_size = 1
            while slow != fast:
                loop_size += 1
                slow = slow.next
            return loop_size
    else:
        return False
