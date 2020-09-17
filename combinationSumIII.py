# Find all possible combinations of k numbers that add up to a
# number n, given that only numbers from 1 to 9 can be used and
# each combination should be a unique set of numbers.
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return_list = []
        while True:
            combo = next(self.list_generator(k))
            if sum(combo) == n and combo not in return_list:
                return_list.append(combo)

    def list_generator(self, list_length):
        yield from combinations(range(1, 9), list_length)

