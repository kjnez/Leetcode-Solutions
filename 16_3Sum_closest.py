from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return res
        return res
