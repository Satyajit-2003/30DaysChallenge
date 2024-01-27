import heapq
from typing import Optional, List

# Put the first value of each list in a min heap
# Pop the min value and add it to the result list
# Add the next value of the list that the min value came from to the heap
# Repeat until all lists are empty

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = curr = ListNode()
        for k in range(len(lists)):
            if lists[k]:
                heapq.heappush(heap, [lists[k].val, k])
                lists[k] = lists[k].next
        
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            if lists[idx]:
                heapq.heappush(heap, [lists[idx].val, idx])
                lists[idx] = lists[idx].next
        
        return dummy.next