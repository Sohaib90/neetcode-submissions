class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mini = 1001
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < mini: mini = nums[mid]
            if nums[right] < nums[mid]:
                left = mid +1
            else: 
                right = mid - 1
        
        return mini