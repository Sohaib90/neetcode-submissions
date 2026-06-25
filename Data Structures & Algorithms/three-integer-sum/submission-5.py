class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            main_num = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + main_num
                seen_nums = tuple([main_num, nums[left], nums[right]])
                if total == 0 and seen_nums not in seen:
                    res.append([main_num, nums[left], nums[right]])
                    seen.add(seen_nums)
                    left +=1
                    right -=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        
        return res