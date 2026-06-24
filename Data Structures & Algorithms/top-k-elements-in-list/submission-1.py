class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for key, val in hashMap.items():
            freq[val].append(key)

        for i in range(len(freq)-1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res

        
        # sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)