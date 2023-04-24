"""
141. Linked List Cycle
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again
    by continuously following the next pointer. Internally, pos is used to denote the index of the node
    that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.
"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def has_cycle(head: ListNode):
    """
    start time: 12:40
    end time: 12:52
    method complexity: Runtime 58 ms; Memory 17.8 MB
    """
    cur = head
    used = set()
    while cur:
        if cur not in used:
            used.add(cur)
            cur = cur.next
        else:
            return True
    return False


if __name__ == '__main__':
    cycle = ListNode(2)
    cycle.next = ListNode(0, ListNode(-4, cycle))
    head1 = ListNode(3, cycle)
    print('actual {} expected True'.format(has_cycle(head1)))
