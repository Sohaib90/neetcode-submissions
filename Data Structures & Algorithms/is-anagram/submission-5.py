class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count_arr = [0] * 26

        for i in range(len(s)):
            count_arr[ord(s[i]) - ord('a')]+=1
            count_arr[ord(t[i]) - ord('a')]-=1 

        for i in range(len(count_arr)):
            if not count_arr[i] == 0:
                return False
        
        return True