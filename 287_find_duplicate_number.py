from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        while l < r:
            m, count = (l + r) // 2, 0
            for n in nums:
                if n <= m:
                    count += 1
            if count <= m:
                l = m + 1
            else:
                r = m
        return r

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
