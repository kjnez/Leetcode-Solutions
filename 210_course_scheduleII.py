from collections import *
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = defaultdict(list)
        for a, b in prerequisites:
            req[a] += b,
        ans, visited = [], [0] * numCourses
        def dfs(x):
            if visited[x] == 1: return True
            if visited[x] == -1: return False
            visited[x] = -1
            if any(not dfs(u) for u in req[x]): return False
            visited[x] = 1
            ans.append(x)
            return True
        return all(dfs(y) for y in range(numCourses)) and ans or []
