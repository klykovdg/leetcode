from typing import Optional
"""
203. Remove Linked List Elements
    Given the head of a linked list and an integer val,
    remove all the nodes of the linked list that has Node.val == val, and return the new head.

    Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

    Example 2:
    Input: head = [], val = 1
    Output: []

    Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

    Constraints:
    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50
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


def remove_elments(head: Optional[ListNode], val):
    """
    start time: 1:57
    end time: 3:00
    method complexity: Runtime 75 ms; Memory 17.1 MB
    """
    prev = None
    cur = head
    while cur:
        if cur.val != val:
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
    func = remove_elments
    head1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(6)))))
    head2 = ListNode(7, ListNode(7, ListNode(7)))
    print('actual {} expected [1, 2, 3]'.format(func(head1, 6)))
    print('actual {} expected None'.format(func(head2, 7)))
