class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = '' 
        count = 0 
        while count < min(len(word1), len(word2)):
            result+=word1[count]
            result+= word2[count]
            count+=1
        if count>= len(word1):
            result+= word2[count:]
        if count>= len(word2):
            result+= word1[count:]
        return result
        