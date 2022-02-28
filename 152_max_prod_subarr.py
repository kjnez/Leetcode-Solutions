from collections import *
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxN = rmaxN = -10
        cur = 1
        for x in nums:
            cur *= x
            maxN = max(maxN, cur)
            if cur == 0: cur = 1
        cur = 1
        for y in reversed(nums):
            cur *= y
            rmaxN = max(rmaxN, cur)
            if cur == 0: cur = 1
        return max(maxN, rmaxN)

    def test(self):
        nums1 = [2,3,-2,4]
        nums2 = [-2,0,-1]
        nums3 = [-2,-3,-4]
        assert self.maxProduct(nums1) == 6
        assert self.maxProduct(nums2) == 0
        assert self.maxProduct(nums3) == 12

sol = Solution()
sol.test()
