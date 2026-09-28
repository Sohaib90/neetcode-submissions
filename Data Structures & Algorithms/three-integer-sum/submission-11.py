class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seen = set()
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]: continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = num + nums[left] + nums[right]
                if s == 0 :
                    if (num, nums[left], nums[right]) not in seen:
                        res.append([num, nums[left], nums[right]])
                        seen.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left +=1
                else:
                    right -= 1
        
        return res