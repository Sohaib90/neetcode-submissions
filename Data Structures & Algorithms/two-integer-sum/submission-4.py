class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)
        res = []

        for i, num in enumerate(nums):
            if target - num in hashMap:
                j = hashMap[target - num]
                if i < j:
                    res.append(i)
                    res.append(j)
                elif i > j:
                    res.append(j)
                    res.append(i)
            else:
                hashMap[num] = i
        
        return res
