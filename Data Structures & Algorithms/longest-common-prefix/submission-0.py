class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        n = 0
        minn = min(strs, key=len)
        while n < len(minn):
            for s in strs:
                if s[n] != minn[n]:
                    return result
            result += minn[n]
            n += 1
        return result
