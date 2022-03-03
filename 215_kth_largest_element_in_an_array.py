from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums,reverse=True)[k-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.nlargest takes O(nlog(k))
        return heapq.nlargest(k, nums)[-1]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        # heapq.heapify takes linear time
        heapq.heapify(h)
        for n in nums[k:]:
            if n > h[0]:
                heapq.heapreplace(h, n)
        return h[0]
