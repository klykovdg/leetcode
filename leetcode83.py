"""
83. Remove Duplicates from Sorted List
    Given the head of a sorted linked list,
    delete all duplicates such that each element appears only once.
    Return the linked list sorted as well.

    Example 1:
    Input: head = [1,1,2]
    Output: [1,2]

    Example 2:
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

    Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next

        return str(result)


def del_duplicates(head: ListNode):
    """
    start time: 20:16
    end time: 20:23
    method complexity: Runtime 37 ms; Memory 13.9 MB
    """
    prev = None
    cur = head
    while cur:
        if prev is None or cur.val != prev.val:
            prev = cur
            cur = cur.next
        else:
            if cur.next:
                cur.val = cur.next.val
                cur.next = cur.next.next
            else:
                if prev:
                    prev.next = None
                else:
                    head = None
                cur = None

    return head


if __name__ == '__main__':
    head1 = ListNode(1, ListNode(1, ListNode(2)))
    head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print('actual {} expected [1, 2]'.format(del_duplicates(head1)))
    print('actual {} expected [1, 2, 3]'.format(del_duplicates(head2)))
