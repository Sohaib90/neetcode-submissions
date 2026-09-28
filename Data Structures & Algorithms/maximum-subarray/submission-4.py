class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        maxSum = -10001

        for i in range(len(nums)):
            curr_sum += nums[i]
            maxSum = max(curr_sum, maxSum)

            if curr_sum < 0:
                curr_sum = 0
        
        return maxSum
