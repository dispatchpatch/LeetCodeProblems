# This file represents the initial solution that I came up with
from typing import Optional

from utilities.ListNode import ListNode



class Solution:
    @staticmethod
    def detect_cycle_first_attempt(head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force Solution
        seen_nodes = {}
        curr = head
        while curr is not None:
            if curr.val in seen_nodes:
                return seen_nodes[curr.val]
            seen_nodes[curr.val] = curr
            curr = curr.next
        # The return None is not required, but I think it improves readability
        return None
    
    # This solution worked for only 6 of 17 test cases in the problem set. This is not ideal obviously.
    # After reviewing the Editorial, I discovered the mistake that I made
    # I had been confused about what would denote equality between two node. I initially thought that is
    # would be if two list nodes had the save value, but this caused problems once there were multiple
    # nodes withe the same value. I realize now that I should have used a simple equality check between the ndes
    # This would work to identify the same node, since multiple references to the node would be the same address
    # in memory. 
    # The improved solution is below

    def detect_cycle_improved(head: Optional[ListNode]) -> Optional[ListNode]:
        seen_nodes = set()
        curr = head
        while curr is not None:
            if curr.next in seen_nodes:
                return curr.next
            seen_nodes.add(curr)
            curr = curr.next
        return None
    
    # The above solution does work, but is not memory efficient since in
    # worst case, it will require all of the nodes in the linked list
    # going into the set. This leads me to another aspect that I had failed to
    # consider in my initial solution, and this is the use of pointers.
    # Using a pointer that races ahead of a second point until it will eventually
    # either reach the end of the list or catch back up the slower point in the case
    # where there is a cycle. In the editorial, these were referred to as tortoise and hare,
    # so I will use the same names here
    @staticmethod
    def detect_cycle_two_point(head: Optional[ListNode]) -> Optional[ListNode]:
        def overlap():
            tort = hare = head
            while hare and hare.next:
                tort = tort.next
                hare = hare.next.next
                if tort == hare:
                    return hare
            return None
    
        if not head:
            return head
        
        overlap_node = overlap()
        if not overlap_node:
            return overlap_node
        
        curr = head
        while curr != overlap_node:
            curr = curr.next
            overlap_node = overlap_node.next
        return curr
        