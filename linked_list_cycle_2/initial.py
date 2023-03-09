# This file represents the initial solution that I came up with
from typing import Optional

from Utils.ListNode import ListNode


class Solution:
    def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force Solution
        seen_nodes = {}
        curr = head
        i = 0
        while not curr is None:
            if curr.val in seen_nodes.keys():
                return seen_nodes[curr.val]
            seen_nodes[curr.val] = curr
            curr = curr.next