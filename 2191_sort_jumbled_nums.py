from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []
        for i, n in enumerate(nums):
            if n == 0:
                mapped += (mapping[n], i),
                continue
            base = 1
            new = 0
            while n:
                d = n % 10
                new += base * mapping[d]
                base *= 10
                n //= 10
            mapped += (new, i),
        mapped.sort()
        ans = []
        for _, j in mapped:
            ans.append(nums[j])
        return ans
