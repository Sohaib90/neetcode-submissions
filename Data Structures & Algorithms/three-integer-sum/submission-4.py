class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            main_num = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + main_num
                if total == 0 and [main_num, nums[left], nums[right]] not in res:
                    res.append([main_num, nums[left], nums[right]])
                    left +=1
                    right -=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        
        print (res)
        return res