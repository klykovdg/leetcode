"""
125. Valid Palindrome
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
"""


def is_palindrome(s: str):
    """
    start time: 14:20
    end time: 14:45
    method complexity: Runtime 42 ms; Memory 14.5 MB
    """
    import string
    s = s.replace(" ", '').lower()
    reply = True
    left = 0
    right = -1
    while -right + left < len(s):
        l = s[left]
        r = s[right]
        if l in string.punctuation:
            left += 1
            continue
        if r in string.punctuation:
            right -= 1
            continue
        if l != r:
            reply = False
            break
        left += 1
        right -= 1

    return reply


if __name__ == '__main__':
    print('actual {} expected True'.format(is_palindrome("A man, a plan, a canal: Panama")))
    print('actual {} expected False'.format(is_palindrome("race a car")))
    print('actual {} expected True'.format(is_palindrome(" ")))
