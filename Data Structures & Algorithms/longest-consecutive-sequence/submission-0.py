class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                temp_longest = 0
                while (num + temp_longest) in numSet:
                    temp_longest += 1

                longest = max(temp_longest, longest)
        
        return longest