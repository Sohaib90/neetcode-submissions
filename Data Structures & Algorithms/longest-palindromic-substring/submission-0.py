class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSub = -1
        subStr = ""

        def mid_palindrome(l, r):
            subLen = 0
            StrSub = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if l == r : 
                    StrSub += s[l]
                    subLen+=1
                else: 
                    StrSub = s[l] + StrSub + s[r]
                    subLen += 2
                l -= 1
                r += 1
            
            return subLen, StrSub
        
        for i, char in enumerate(s):
            sublen1, substr1 = mid_palindrome(i, i)
            sublen2, substr2 = mid_palindrome(i, i + 1)

            if sublen1 > sublen2 and sublen1 > maxSub:
                maxSub = sublen1
                subStr = substr1
            elif sublen2 >= sublen1 and sublen2 > maxSub:
                maxSub = sublen2
                subStr = substr2
            
        return subStr
            
            