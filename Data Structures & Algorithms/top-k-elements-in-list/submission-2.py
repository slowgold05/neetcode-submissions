class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result =[]
        for ele in nums: 
            if ele in freq: 
                freq[ele]+=1
            else:
                freq[ele]=1
        while k>0:
            max_val = max(freq.values())
            for key,value in freq.items():
                if value == max_val:
                    result.append(key)
                    freq[key] = 0
                    break
            k-=1
                
        
        return result
        