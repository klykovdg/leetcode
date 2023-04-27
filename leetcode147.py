"""
147. Insertion Sort List
    Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

    The steps of the insertion sort algorithm:
    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs
    within the sorted list and inserts it there.
    It repeats until no input elements remain.

    Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

    Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]
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


def insertion_sort_list(head: ListNode) -> ListNode:
    """
    start time: 13:27
    end time: 15:17
    method complexity: time limit exceeded
    """
    cur, prev = head, None
    p = {}
    while cur:
        if prev is None or cur.val >= prev.val:
            p[cur.val] = prev
            prev = cur
            cur = cur.next
        else:
            temp_cur = cur.next
            temp_prev = prev
            while 1:
                x = p[prev.val]
                if x is None or cur.val >= x.val:
                    if x is None:
                        head = cur
                    else:
                        x.next = cur
                    p[cur.val] = x
                    p[prev.val] = cur
                    cur.next = prev
                    break
                else:
                    prev = x
            cur = temp_cur
            prev = temp_prev
            prev.next = cur
    return head


def insertion_sort_list2(head: ListNode) -> ListNode:
    """
    start time: 21:56
    end time: 22:19
    method complexity: Runtime 53 ms; Memory 16.7 MB
    """
    cur, prev = head, None
    p = []
    while cur:  # O(N)
        if prev is None or cur.val >= prev.val:
            p.append(cur)
            prev = cur
            cur = cur.next
        else:
            index = find(p, cur)  # O(logN)
            p.insert(index, cur)  # O(N) given that the list increases gradually (n*(n+1)/2)
            prev.next = cur.next
            cur.next = p[index + 1]  # won't be an index out of bound exception due to 80th line
            if index != 0:
                p[index - 1].next = cur
            cur = prev.next

    return p[0]


def find(arr: list, node: ListNode) -> int:
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (right + left) // 2
        if node.val <= arr[mid].val:
            right = mid
        else:
            left = mid

    return left + 1


if __name__ == '__main__':
    head = ListNode(4, ListNode(5, ListNode(2, ListNode(1, ListNode(3)))))
    func = insertion_sort_list2
    print('actual {} expected [1, 2, 3, 4, 5]'.format(func(head)))

    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print('actual {} expected [-1, 0, 3, 4, 5]'.format(func(head)))

    head = ListNode(3, ListNode(2, ListNode(4)))
    print('actual {} expected [2, 3, 4]'.format(func(head)))
