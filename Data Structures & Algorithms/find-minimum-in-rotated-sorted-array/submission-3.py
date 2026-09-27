class Solution:
    def findMin(self, nums: List[int]) -> int:
        minnum = 1001
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                minnum = nums[i+1]
                break
        
        if minnum == 1001: return nums[0]
        return minnum
