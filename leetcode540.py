"""
540. Single Element in a Sorted Array
    You are given a sorted array consisting of only integers
    where every element appears exactly twice,
    except for one element which appears exactly once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.

    Example 1:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

    Example 2:
    Input: nums = [3,3,7,7,10,11,11]
    Output: 10

    Constraints:
    1 <= nums.length <= 105
    0 <= nums[i] <= 105
"""


def single_num(nums: list):
    """
    First solution
    start time: 03:09
    end time: 03:11
    method complexity: Runtime 169 ms; Memory 23.8 MB
    """
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


def single_num2(nums: list):
    """
    Second solution
    start time: 03:55
    end time: 04:03
    method complexity: Runtime 171 ms; Memory 23.6 MB
    """
    if len(nums) == 1:
        return nums[0]
    for i in range(1, len(nums), 2):
        if nums[i] != nums[i - 1]:
            return nums[i - 1]
    return nums[-1]  # in case the searched elm will be the last one


def single_num3(nums: list):
    """
    Third solution
    start time: 04:08
    end time: 05:18
    method complexity: Runtime 165 ms; Memory 23.8 MB
    """
    if len(nums) == 1:
        return nums[0]
    left = -1
    right = len(nums)

    while right - left > 1:
        mid = (left + right) // 2
        if mid % 2 != 0:
            if nums[mid - 1] == nums[mid]:
                left = mid + 1
            else:
                right = mid
        else:
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

    return nums[left] if left != -1 else nums[left + 1]


if __name__ == '__main__':
    func = single_num3
    print('actual {} expected 13'.format(func([1, 1, 2, 2, 3, 3, 4, 4, 8, 8, 9, 9, 11, 11, 13])))
    print('actual {} expected 1'.format(func([1, 2, 2, 3, 3, 4, 4, 8, 8, 9, 9, 11, 11, 13, 13])))
    print('actual {} expected 2'.format(func([1, 1, 2, 3, 3])))
    print('actual {} expected 10'.format(func([3, 3, 7, 7, 10, 11, 11])))
    print('actual {} expected 2'.format(func([2])))
    print('actual {} expected 14'.format(func([3, 3, 7, 7, 10, 10, 11, 11, 14])))
    print('actual {} expected 1'.format(func([1, 3, 3, 7, 7, 11, 11])))
