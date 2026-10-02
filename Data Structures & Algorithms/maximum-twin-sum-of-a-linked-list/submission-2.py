# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first = head
        second = prev
        maxTsum = 0

        while first and second:
            maxTsum = max(maxTsum, first.val + second.val)
            first = first.next
            second = second.next
        
        return maxTsum
