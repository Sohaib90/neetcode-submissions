class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_array = []
        left = 0
        right = len(nums) - 1
        
        for i, num in enumerate(nums):
            index_array.append((num, i))
        
        index_array.sort()
        while left < right:
            if index_array[left][0] + index_array[right][0] == target:
                if index_array[left][1] < index_array[right][1]:
                    return [index_array[left][1], index_array[right][1]]
                else:
                    return [index_array[right][1], index_array[left][1]]
            elif index_array[left][0] + index_array[right][0] > target:
                right = right - 1
            else:
                left = left + 1
    
        return []

        
