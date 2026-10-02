# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []

        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
        
        maxTsum = 0
        n = len(array)
        if (n // 2) - 1 <= 0:
            return sum(array)

        for i in range((n // 2)):
            maxTsum = max(maxTsum, array[i] + array[n - 1 - i])

        
        return maxTsum

