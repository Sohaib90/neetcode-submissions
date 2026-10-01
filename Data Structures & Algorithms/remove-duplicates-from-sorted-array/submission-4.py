class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = 1
        prev = nums[0]
        L = 0 
        index = 1

        for n in range(1, len(nums)):
            if nums[n] == prev:
                while n < len(nums) and nums[n] == prev:
                    n += 1
            else:
                prev = nums[n]
                nums[index] = nums[n]
                unique_nums += 1
                index += 1
        
        return unique_nums
            
            