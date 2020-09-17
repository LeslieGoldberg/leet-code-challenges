# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
import math


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_list = [int(num) for num in nums]
        nums_list_sorted = sorted(nums_list)
        subarray_options = [num for num in nums_list]

        product = max(map(math.prod, subarray_options))
        return product
