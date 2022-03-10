from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i < 0 and j >= 0:
                return 0
            if j < 0:
                return 1
            if s[i] != t[j]:
                return dp(i-1, j)
            else:
                return dp(i-1, j-1) + dp(i-1, j)
        return dp(len(s) - 1, len(t) - 1)
