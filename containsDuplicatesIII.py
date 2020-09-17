# Given an array of integers, find out whether there are two distinct indices i and j in the array
# such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference
# between i and j is at most k.

import itertools

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        is_duplicate = False
        if len(nums) == 1:
            pass
        else:
            for couple in self.index_comb_generator(nums, k):
                if abs(nums[couple[0]] - nums[couple[1]]) <= t:
                    is_duplicate = True
                    break

        return is_duplicate

    def index_comb_generator(self, nums, k):
        nums_length = len(nums)
        r = range(nums_length)
        for tup in itertools.combinations(range(nums_length), 2):
            if abs(tup[0] - tup[1]) <= k:
                yield tup

s = Solution()
s.containsNearbyAlmostDuplicate([2, 2], 3, 0)