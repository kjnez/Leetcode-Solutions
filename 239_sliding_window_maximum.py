from sortedcontainers import SortedList
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sl = SortedList(nums[:k])
        for i in range(len(nums) - k + 1):
            if i > 0:
                sl.remove(nums[i-1])
                sl.add(nums[i+k-1])
            ans.append(sl[-1])
        return ans
    def maxSlidingWindow(self, nums, k):
        q = collections.deque() # store indices
        ans = []
        for i, n in enumerate(nums):
            while q and nums[q[-1]] <= n:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
