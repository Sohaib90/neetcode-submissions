class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res: dict = {}
        res_arr = []
        for i, _ in enumerate(strs):
            key = "".join(sorted(strs[i]))
            if not key in res: 
                res[key] = [strs[i]]
                for k in range(i + 1, len(strs)):
                    match = "".join(sorted(strs[k]))
                    if key == match:
                        res[key].append(strs[k])
            else:
                continue

        for key, val in res.items():
            if len(val):
                res_arr.append(val)

        return res_arr        
        

