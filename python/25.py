# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        
        # count the length of the linked list
        while curr and count != k:
            curr = curr.next
            count += 1
        
        # if the length is less than k, return head
        if count < k:
            return head
        
        # reverse the first k nodes
        curr = self.reverseKGroup(curr, k)
        
        # reverse the remaining nodes
        while count:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
            count -= 1
        
        return curr