class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro = nums[0]
        currentMax = maxPro
        currentMin = maxPro

        for i in range(1, len(nums)):
            current = nums[i]
            prev_max = currentMax
            currentMax = max(current, prev_max * current, currentMin * current)
            currentMin = min(current, prev_max * current, currentMin * current)

            if currentMax > maxPro:
                maxPro = currentMax
        
        return maxPro