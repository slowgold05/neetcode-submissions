class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)*2):
            result.append(" ")
        for i in range(len(nums)):
            result[i] = nums[i]
            result[i+len(nums)] = nums[i]
        return result
            