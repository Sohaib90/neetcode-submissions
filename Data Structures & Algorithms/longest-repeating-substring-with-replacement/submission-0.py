class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find_max_frequency(dic):
            freq = 0

            for key, val in dic.items():
                if val > freq:
                    freq = val 
            
            return freq

        count = defaultdict(int)
        l = 0
        r = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if r - l + 1 - find_max_frequency(count) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res
