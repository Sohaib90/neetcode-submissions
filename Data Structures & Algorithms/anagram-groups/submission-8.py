class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        newstr = [" "]* len(strs)
        for i in range(len(strs)):
            newstr[i] = "".join(sorted(strs[i]))
        
        res = defaultdict(list)
        for i in range(len(strs)):
            res[newstr[i]].append(strs[i])
        
        return list(res.values())
        

            