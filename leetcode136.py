"""
136. Single Number
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Example 1:
    Input: nums = [2,2,1]
    Output: 1

    Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

    Example 3:
    Input: nums = [1]
    Output: 1
"""


def single_num(nums: list) -> int:
    """
    First solution
    start time: 18:06
    end time: 18:28
    method complexity: Runtime 133 ms; Memory 17 MB
    """
    s = set()  # maybe violate the rule 'use only constant extra space'
    for i in nums:
        if i in s:
            s.remove(i)
        else:
            s.add(i)

    return s.pop()


def single_num2(nums: list) -> int:
    """
    Second solution
    start time: 18:45
    end time: 18:15
    method complexity: Runtime 135 ms; Memory 16.7 MB
    """
    nums.sort()  # maybe violate the rule 'with a linear runtime complexity'
    odd_flag = True
    if len(nums) > 1:
        for i in nums:
            if odd_flag:
                first_cur_elm = i
                odd_flag = False
            else:
                odd_flag = True
                if i != first_cur_elm:
                    return first_cur_elm
    else:
        return nums[0]
    return first_cur_elm  # in case the searched elm will be the last one


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 6, 7, 8, 9]  # 5
    arr2 = [2,2,1]  # 1
    arr3 = [4,1,2,1,2]  # 4
    arr4 = [1]  # 1
    for arr, expected in (arr1, 5), (arr2, 1), (arr3, 4), (arr4, 1):
        print('actual {} expected {}'.format(single_num(arr), expected))
        print('actual {} expected {}'.format(single_num2(arr), expected))
