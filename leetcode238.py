"""
238. Product of Array Except Self
    Given an integer array nums, return an array answer such that
    answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
"""


def pes(nums: list) -> list[int]:
    """
    start time: 13:00
    end time: 14:00
    Time Limit Exceeded (18/22 tests passed)
    """
    arr = [1,]
    for k in range(len(nums) - 1):
        arr.append(arr[k] * nums[k])

    for i in range(len(arr) - 1):          # index arr
        for j in range(i + 1, len(nums)):  # index nums
            arr[i] *= nums[j]

    return arr


def pes2(nums: list) -> list[int]:
    """
    I've watched the video https://www.youtube.com/watch?v=bNvIQI2wAjk
    """
    result = []
    prefix = 1
    for i in range(len(nums)):
        result.append(prefix)
        prefix *= nums[i]

    postfix = 1
    for i in range(-1, -len(nums) - 1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


if __name__ == '__main__':
    func = pes2
    print('act {}\nexp [60, 40, 30, 24]\n'.format(func([2,3,4,5])))
    print('act {}\nexp [24, 12, 8, 6]\n'.format(func([1,2,3,4])))
    print('act {}\nexp [0, 0, 9, 0, 0]\n'.format(func([-1,1,0,-3,3])))
    print('act {}\nexp [4, 3]\n'.format(func([3, 4])))
