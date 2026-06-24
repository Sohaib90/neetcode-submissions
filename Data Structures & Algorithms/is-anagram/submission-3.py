class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countCheck: dict  = {}
        if not len(s) == len(t):
            return False

        for char in s:
            if char in countCheck:
                countCheck[char]+=1
            else:
                countCheck[char] = 1
        
        for char in t:
            if char in countCheck:
                countCheck[char]-=1
            else:
                return False
        
        for key, val in countCheck.items():
            if val:
                return False
        
        return True
