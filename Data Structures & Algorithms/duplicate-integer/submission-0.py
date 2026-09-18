class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d_num = {}
        for ele in nums: 
            if ele in d_num:
                d_num[ele]+=1
                return True
            else:
                d_num[ele] = 1
        return False

        