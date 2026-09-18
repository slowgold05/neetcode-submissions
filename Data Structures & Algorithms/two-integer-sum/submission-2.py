class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in num:
                return [num[need], i]

            num[nums[i]] = i
        