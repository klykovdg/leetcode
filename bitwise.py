from math import log2, ceil
"""
1. For any number, we can check whether its ‘i’th bit is 0(OFF)
   or 1(ON) by bitwise ANDing it with “2^i” (2 raise to i).
2. Write an efficient program to count the number of 1s in the binary representation of an integer.

3. Given a number x and two positions (from the right side) in the binary representation of x,
   write a function that swaps n bits at the given two positions and returns the result.
   It is also given that the two sets of bits do not overlap.

4. Given two integers, find XOR of them without using the XOR operator, i.e., without using ^ in C/C++.
"""


def count_number_1_in_binary_int(i: int):
    """
    start time: 15:00
    end time: 15:01
    method complexity: O(N)
    """
    return bin(i).count('1')


def count_number_1_in_binary_int2(i: int):
    """
    start time: 15:01
    end time: 16:00
    method complexity: O(N)
    """
    result = 0
    count_bit = ceil(log2(i + 1))
    for k in range(count_bit):  # O(N)
        p = pow(2, k)           # O(1)
        if p & i:
            result += 1

    return result


def swap(i: int, pos1, pos2):
    """
    pos1 and pos2 are positive indexes
    from the right side of the binary repr of given int from 0

    start time: 16:20
    end time: 16:54
    """
    pos1 = -pos1 - 1
    pos2 = -pos2 - 1
    s = bin(i)
    start = s[:pos2]
    if pos1 == -1:
        mid = s[pos1:pos2 - 1:-1]
        end = ''
    else:
        mid = s[pos1:pos2 - 1:-1]
        end = s[pos1 + 1:]
    result = start + mid + end

    return int(result, 2)


def swap2(x: int, p1, p2):
    """
    Unfortunately, I never work with bits
    From https://www.geeksforgeeks.org/swap-bits-in-a-given-number/
    """
    s = bin(x)
    n = p2 - 1 - p1
    set1 = (x >> p1) & ((1 << n) - 1)
    set2 = (x >> p2) & ((1 << n) - 1)
    xor = (set1 ^ set2)
    xor = (xor << p1) | (xor << p2)
    result = x ^ xor
    s2 = bin(result)

    return result


def xor_without_xor(i1: int, i2: int):
    """
    start time: 17:25
    end time: 18:11
    """
    l = max(len(bin(i1)), len(bin(i2))) - 2
    s1 = bin(i1)[2:].zfill(l)
    s2 = bin(i2)[2:].zfill(l)
    index = 0
    result = ['0b',]
    while index < len(s1):
        cur = '0' if s1[index] == s2[index] else '1'
        result.append(cur)
        index += 1

    return int(''.join(result), 2)


if __name__ == '__main__':
    func = count_number_1_in_binary_int2
    print('actual {} expected 5'.format(func(789)))
    print('actual {} expected 0'.format(func(0)))
    print('actual {} expected 1'.format(func(1)))
    print('actual {} expected 9'.format(func(3454)))

    print('\nactual {} expected 229'.format(swap(234, 0, 3)))
    print('actual {} expected 156'.format(swap(456, 2, 8)))
    print('actual {} expected 218'.format(swap(234, 4, 5)))

    print('\nactual {} expected 241'.format(swap2(234, 0, 3)))
    print('actual {} expected 4740'.format(swap2(456, 2, 8)))
    print('actual {} expected 234'.format(swap2(234, 4, 5)))

    print('\nactual {} expected {}'.format(xor_without_xor(234, 0), 234 ^ 0))
    print('actual {} expected {}'.format(xor_without_xor(456, 2), 456 ^ 2))
    print('actual {} expected {}'.format(xor_without_xor(12, 239), 12 ^ 239))
