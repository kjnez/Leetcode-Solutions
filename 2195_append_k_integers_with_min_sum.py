from typing import List
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = (k + 1) * k // 2
        for x in sorted(list(set(nums))):
            if x <= k:
                k += 1
                ans += k - x
            else:
                break
        return ans
