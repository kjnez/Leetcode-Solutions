from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        s, p = list(s), Counter(p)
        ans = []
        cur = Counter(s[:m])
        for i in range(len(s) - m + 1):
            if i > 0:
                cur[s[i-1]] -= 1
                cur[s[i+m-1]] += 1
            if p == cur:
                ans.append(i)
        return ans
