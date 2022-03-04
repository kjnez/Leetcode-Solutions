from typing import List
from functools import lru_cache
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        @lru_cache(None)
        def dp(x, y):
            nonlocal ans
            if x < 0 or y < 0:
                return 0
            if x == 0 or y == 0:
                cur = (matrix[x][y] == '1')
                val = cur + min(dp(x-1, y),0) if x > 0 else cur + min(dp(x, y-1),0)
                ans = max(ans, val**2)
                return val
            if matrix[x][y] == '1':
                val = min(dp(x-1, y-1), dp(x-1, y), dp(x, y-1)) + 1
            else:
                val = min(dp(x-1, y-1), dp(x-1, y), dp(x, y-1), 0)
            ans = max(ans, val**2)
            return val
        dp(m-1, n-1)
        return ans
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = [[0 for _ in range(n+1)] for _ in range(m+1)]
        maxL = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    cache[r+1][c+1] = 1 + min(cache[r][c], cache[r][c+1], cache[r+1][c])
                    maxL = max(maxL, cache[r+1][c+1])
        return maxL**2
