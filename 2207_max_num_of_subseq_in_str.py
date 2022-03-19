class Solution:
    def maximumSubsequenceCount(self, s: str, p: str) -> int:
        cnt1 = cnt2 = ans = 0
        for c in s:
            if c == p[1]:
                ans += cnt1
                cnt2 += 1
            if c == p[0]:
                cnt1 += 1
        return ans + max(cnt1, cnt2)
