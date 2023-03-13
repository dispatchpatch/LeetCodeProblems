from typing import List, Optional

from utilities.ListNode import ListNode


class Solution:
    @staticmethod
    def merge_k_lists_sort_and_remove(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # First thought
        # sort list of pointers in ascending order of their head
        # add head of first pointer to the new list
        # return the head of that linked list
        head = None
        prev = None
        while len(lists):
            lists = [curr for curr in lists if curr is not None]
            lists = sorted(lists, key=lambda curr: curr.val)
            if not lists:
                return head
            
            next_node = lists[0]
            if head is None:
                head = next_node
                prev = head
            else:
                prev.next = next_node
                prev = next_node
            lists[0] = lists[0].next
        return head

    # The above solution works! And on the first try too! But it is exceptionally slow.
    # It ranks in the bottom 5% of all of the challenges that were submitted
    # I think that part of the reason that it is so slow is that I'm sorting the list every time, 
    # instead I think I should just loop through all of the nodes and then just add the lowest value node
    @staticmethod
    def merge_k_lists_find_lowest(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        prev = None

        if not lists:
            return None
            
        while True:
            idx = 0
            lowest = lists[0]
            for curr in lists:
                if curr is None:
                    continue
                if lowest is None or curr.val < lowest.val:
                    idx = lists.index(curr)
                    lowest = curr
            if lowest is None:
                break
            
            if head is None:
                head = lowest
                prev = head
            else:
                prev.next = lowest
                prev = lowest
            lists[idx] = lowest.next
        return head

    # This above solution doesn't run any faster
    # Let's try writing the algorithm for doing merging 2 linked lists
    # Then just loop through groups of two in the List of nodes until it works out
    @staticmethod
    def merge_k_lists_merge_2(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_2_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # Creating our initial nodes like this means that we 
            # will never have to worry about curr or head being None
            head = curr = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            if list1 and not list2:
                curr.next = list1
            if list2 and not list1:
                curr.next = list2
            
            return head.next

        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None if i + 1 == len(lists) else lists[i + 1]
                l3 = merge_2_lists(l1, l2)
                temp.append(l3)
            lists = temp
        return lists[0]
    
    # This last attempt runs much faster because we are just merging a lot of lists, which take log(n) time