# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        dummy = temp
        for i in lists:
            while i:
                temp.append(i.val) 
                i = i.next
        temp.sort()
        
        res = ListNode()
        dummy = res
        for i in temp:
            res.next = ListNode(i)
            res = res.next

        return dummy.next

