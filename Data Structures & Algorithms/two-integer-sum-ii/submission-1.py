class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = defaultdict(int)
        res = []
        for i in range(len(numbers)):
            curr = numbers[i]
            if target - curr in count:
                res.append(count[target - curr])
                res.append(i + 1)
            else:
                count[curr] = i + 1
        print(res)
        return res
