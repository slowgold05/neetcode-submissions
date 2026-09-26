class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ele in s: 
            if ele.isalnum():
                result+=ele.lower()
        print(result)
        print(result[::-1])
        if result == result[::-1]:
            return True
        return False
        