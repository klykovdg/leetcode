import re
"""
387. First Unique Character in a String
    Given a string s, find the first non-repeating character in it and return its index.
    If it does not exist, return -1

    Example 1:
    Input: s = "leetcode"
    Output: 0

    Example 2:
    Input: s = "loveleetcode"
    Output: 2

    Example 3:
    Input: s = "aabb"
    Output: -1
"""


def first_uniq_char(string: str):
    """
    start time: 23:04
    end time: 23:38
    method complexity: Runtime 91 ms; Memory 14.2 MB
    """
    arr = {}
    for pos, s in enumerate(string):
        if s not in arr:
            arr[s] = [True, pos]
        else:  # if have duplicate
            arr[s][0] = False

    min_id = -1
    for letter in arr.values():
        if letter[0]:  # if unique
            if letter[1] < min_id or min_id == -1:
                min_id = letter[1]

    return min_id


if __name__ == '__main__':
    print('actual %d expected 9' % first_uniq_char("aabbbaabbiaabbaabbbb"))
    print('actual %d expected 0' % first_uniq_char("leetcode"))
    print('actual %d expected 2' % first_uniq_char("loveleetcode"))
    print('actual %d expected -1' % first_uniq_char("aabb"))
    print('actual %d expected 0' % first_uniq_char("a"))
    print('actual %d expected 4' % first_uniq_char("aavvr"))
