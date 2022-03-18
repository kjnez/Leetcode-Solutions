from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i, curSum=0):
            if i < 0:
                if curSum == target:
                    return 1
                else:
                    return 0
            minusCur = dp(i-1, curSum-nums[i])
            plusCur = dp(i-1, curSum+nums[i])
            return minusCur + plusCur
        return dp(len(nums)-1)
