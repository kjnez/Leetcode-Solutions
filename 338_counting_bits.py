from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = 0
            while i:
                i = i & (i - 1)
                count += 1
            ans.append(count)
        return ans
