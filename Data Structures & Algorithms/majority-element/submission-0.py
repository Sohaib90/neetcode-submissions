class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tempdict = defaultdict(int)

        for num in nums:
            tempdict[num]+=1

        for key, val in tempdict.items():
            if val > len(nums) // 2:
                return key
