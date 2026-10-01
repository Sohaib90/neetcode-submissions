class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minL = float("inf")
        L = 0
        total = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minL = min(minL, R - L + 1)
                total = total - nums[L]
                L += 1   
            
        return 0 if minL == float("inf") else minL