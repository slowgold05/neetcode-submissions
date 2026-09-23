class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        current = {}
        result =[]
        for ele in strs:
            curr = ''.join(sorted(ele))
            if curr in current:
                current[curr].append(ele)
            else:
                current[curr] = [ele]
        for key,value in current.items():
            result += [value]
        return result

        