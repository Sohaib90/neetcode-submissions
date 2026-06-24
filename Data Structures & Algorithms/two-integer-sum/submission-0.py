class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap: dict = {}
        for i, num in enumerate(nums):
            if (target - num) in sumMap:
                return [sumMap[target-num], i]
            else:
                sumMap[num] = i
                print(sumMap)