class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        length = min(len(str) for str in strs)
        for i in range(length):
            s = strs[0][i]
            if all(str[i] == s for str in strs):
                prefix += s
            else:
                break
        return prefix
