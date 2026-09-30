class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLen = len(s1)
        if len(s1) > len(s2): return False
        l = 0
        r = windowLen - 1
        s1Sort = "".join(sorted(s1))

        while r < len(s2):
            subStr = s2[l : r + 1]
            if s1Sort == "".join(sorted(subStr)):
                return True
            else: 
                l += 1
                r += 1
        
        return False