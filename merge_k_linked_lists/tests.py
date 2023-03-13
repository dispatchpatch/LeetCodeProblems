from typing import List, Optional
import unittest
from merge_k_linked_lists.solution import Solution

from utilities.ListNode import ListNode


class TestMergeKLists_SortAndRemove(unittest.TestCase):
    def test_empty_list(self):
        heads = []
        self.assertIsNone(Solution.merge_k_lists_sort_and_remove(heads))

    def test_list_of_Nones(self):
        heads = [None, None, None]
        self.assertIsNone(Solution.merge_k_lists_sort_and_remove(heads))

    def test_single_list(self):
        l1 = build_list([1, 2, 3])
        heads = [l1]
        result = Solution.merge_k_lists_sort_and_remove(heads)
        expected_list = build_list([1, 2, 3])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()
    
    def test_two_lists(self):
        l1 = build_list([1, 2, 3])
        l2 = build_list([2, 3, 4])
        heads = [l1, l2]
        result = Solution.merge_k_lists_sort_and_remove(heads)
        expected_list = build_list([1, 2, 2, 3, 3, 4])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()
    
    def test_5_list_with_Nones(self):
        l1 = build_list([1, 2, 3])
        l2 = build_list([2, 3, 4])
        l3 = build_list([1, 4, 6])
        heads = [None, l1, l2, None, l3]
        result = Solution.merge_k_lists_sort_and_remove(heads)
        expected_list = build_list([1, 1, 2, 2, 3, 3, 4, 4, 6])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()

class TestMergeKLists_FindLowest(unittest.TestCase):
    def test_empty_list(self):
        heads = []
        self.assertIsNone(Solution.merge_k_lists_find_lowest(heads))

    def test_list_of_Nones(self):
        heads = [None, None, None]
        self.assertIsNone(Solution.merge_k_lists_find_lowest(heads))

    def test_single_list(self):
        l1 = build_list([1, 2, 3])
        heads = [l1]
        result = Solution.merge_k_lists_find_lowest(heads)
        expected_list = build_list([1, 2, 3])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()
    
    def test_two_lists(self):
        l1 = build_list([1, 2, 3])
        l2 = build_list([2, 3, 4])
        heads = [l1, l2]
        result = Solution.merge_k_lists_find_lowest(heads)
        expected_list = build_list([1, 2, 2, 3, 3, 4])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()
    
    def test_5_list_with_Nones(self):
        l1 = build_list([1, 2, 3])
        l2 = build_list([2, 3, 4])
        l3 = build_list([1, 4, 6])
        heads = [None, l1, l2, None, l3]
        result = Solution.merge_k_lists_find_lowest(heads)
        expected_list = build_list([1, 1, 2, 2, 3, 3, 4, 4, 6])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()


class TestMergeKLists_Merge2(unittest.TestCase):
    def test_empty_list(self):
        heads = []
        self.assertIsNone(Solution.merge_k_lists_merge_2(heads))

    def test_list_of_Nones(self):
        heads = [None, None, None]
        self.assertIsNone(Solution.merge_k_lists_merge_2(heads))

    def test_single_list(self):
        l1 = build_list([1, 2, 3])
        heads = [l1]
        result = Solution.merge_k_lists_merge_2(heads)
        expected_list = build_list([1, 2, 3])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()
    
    def test_two_lists(self):
        l1 = build_list([1, 2, 3])
        l2 = build_list([2, 3, 4])
        heads = [l1, l2]
        result = Solution.merge_k_lists_merge_2(heads)
        expected_list = build_list([1, 2, 2, 3, 3, 4])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()
    
    def test_5_list_with_Nones(self):
        l1 = build_list([1, 2, 3])
        l2 = build_list([2, 3, 4])
        l3 = build_list([1, 4, 6])
        heads = [None, l1, l2, None, l3]
        result = Solution.merge_k_lists_merge_2(heads)
        expected_list = build_list([1, 1, 2, 2, 3, 3, 4, 4, 6])
        while expected_list and result:
            self.assertEqual(result.val, expected_list.val)
            result = result.next
            expected_list = expected_list.next
        else:
            if expected_list or result:
                self.fail()


def build_list(vals: Optional[List[int]]) -> Optional[ListNode]:
    head = curr = ListNode(0)
    for val in vals:
        new_node = ListNode(val)
        curr.next = new_node
        curr = new_node
    return head.next