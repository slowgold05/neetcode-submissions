class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter= {}
        for ele in nums: 
            if ele not in counter:
                counter[ele] = 0
            else: 
                counter[ele] +=1
        return max(counter, key=counter.get)
            