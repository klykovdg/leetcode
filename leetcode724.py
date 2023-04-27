"""
724. Find Pivot Index
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index
    is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array,
    then the left sum is 0 because there are no elements to the left.
    This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

    Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11

    Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.

    Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0
"""


def pivot_id(nums: list) -> int:
    """
    start time: 12:30
    end time: 12:43
    method complexity: Runtime 143 ms; Memory 15 MB
    """
    right_sum = sum(nums)
    left_sum = 0
    for index, i in enumerate(nums):
        right_sum -= i
        if left_sum == right_sum:
            return index
        left_sum += i
    return -1


if __name__ == '__main__':
    func = pivot_id
    print('actual {} expected 3'.format(func([1,7,3,6,5,6])))
    print('actual {} expected -1'.format(func([1,2,3])))
    print('actual {} expected 0'.format(func([2,1,-1])))
    print('actual {} expected 2'.format(func([1, -1, 2])))
