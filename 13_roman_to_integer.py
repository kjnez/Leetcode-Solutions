class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, \
             'M': 1000, 'CM': 900, 'XC': 90, 'IV': 4, 'IX': 9, 'XL': 40, 'CD': 400}
        ans = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in d:
                ans += d[s[i:i+2]]
                i += 2
                continue
            ans += d[s[i]]
            i += 1
        return ans
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i+1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
        return ans + d[s[-1]]
