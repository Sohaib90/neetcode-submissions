class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Map = defaultdict(int)
        unique_nums = 0
        L = 0 
        index = 0

        for n in range(len(nums)):
            if nums[n] in Map:
                while n < len(nums) and nums[n] in Map:
                    n += 1
            else:
                Map[nums[n]] += 1
                nums[index] = nums[n]
                unique_nums += 1
                index += 1
        
        return unique_nums
            
            