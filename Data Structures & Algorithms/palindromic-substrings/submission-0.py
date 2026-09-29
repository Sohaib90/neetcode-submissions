class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def around_centre(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
            return count


        for i,each in enumerate(s):
            res += around_centre(i, i)
            res += around_centre(i, i + 1)
        
        return res