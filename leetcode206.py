"""
206. Reverse Linked List
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:
    Input: head = []
    Output: []
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


def reverse(head: ListNode):
    """
    start time: 21:15
    end time: 21:25
    method complexity: Runtime 22 ms; Memory 15.4 MB
    """
    prev = None
    cur = head
    while cur:
        if prev:
            cur.next, prev, cur = prev, cur, cur.next
            # temp = cur.next
            # cur.next = prev
            # prev = cur
            # cur = temp
        else:
            prev = cur
            cur = cur.next
            prev.next = None

    return prev


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print('actual {} expected [5, 4, 3, 2, 1]'.format(reverse(head)))

    head = ListNode(1, ListNode(2))
    print('actual {} expected [2, 1]'.format(reverse(head)))

    head = ListNode(1)
    print('actual {} expected [1]'.format(reverse(head)))
