# This file represents the initial solution that I came up with
from typing import Optional

from Utils.ListNode import ListNode


class Solution:
    @staticmethod
    def detect_cycle( head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force Solution
        seen_nodes = {}
        curr = head
        while curr is not None:
            if curr.val in seen_nodes:
                return seen_nodes[curr.val]
            seen_nodes[curr.val] = curr
            curr = curr.next
    
    # This solution worked for only 6 of 17 test cases in the problem set. This is not ideal obviously.
    # After reviewing the Editorial, I discovered the mistake that I bad