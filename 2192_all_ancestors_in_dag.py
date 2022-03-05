from typing import List
from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for x, y in edges:
            adj[y] += x,
        
        def dfs(x, visited, anc):
            if x in visited:
                return
            visited.add(x)
            if not adj[x]:
                return
            for u in adj[x]:
                # visited.add(u)
                if u not in visited:
                    anc.append(u)
                    dfs(u, visited, anc)

        ans = []
        for i in range(n):
            visited, anc = set(), []
            dfs(i, visited, anc)
            ans.append(sorted(anc))
        return ans
