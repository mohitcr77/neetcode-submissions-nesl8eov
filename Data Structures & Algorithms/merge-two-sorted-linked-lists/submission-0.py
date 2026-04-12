# Definition for a single piece of the chain (a "Node").
# Imagine each ListNode is like a person holding a number and 
# pointing their hand toward the next person in line.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val    # The number this person is holding
#         self.next = next  # The next person they are pointing to

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a "Fake Starting Point" (Dummy). 
        # This is like placing an empty basket at the start so we have 
        # something to tie our new sorted chain to.
        dummy = ListNode()

        # 2. 'tail' is our "Current End." 
        # Right now, the end of our new chain is just that empty basket.
        tail = dummy

        # 3. Look at both lines (list1 and list2) as long as both have people in them.
        while list1 and list2:
            # Check who has the smaller number.
            if list1.val < list2.val:
                # If list1's person has a smaller number, 
                # add them to our new chain next.
                tail.next = list1
                # Move to the next person in list1's line.
                list1 = list1.next
            else:
                # Otherwise, list2's person is smaller (or the same), 
                # so add them to our chain.
                tail.next = list2
                # Move to the next person in list2's line.
                list2 = list2.next
            
            # After adding a person, our "Current End" (tail) moves 
            # to that new person we just added.
            tail = tail.next

        # 4. What if one line finishes before the other?
        # If there are still people left in list1, just attach the 
        # whole remaining line to our chain.
        if list1:
            tail.next = list1
        # Or, if there are still people left in list2, attach them.
        elif list2:
            tail.next = list2

        # 5. Return the result! 
        # We don't want the "empty basket" (dummy), so we return 
        # everything that comes AFTER it.
        return dummy.next