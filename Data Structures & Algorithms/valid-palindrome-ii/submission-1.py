class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            curr = s[:i] + s[i+1:]
            if curr == curr[::-1]:
                return True
        return False 
        