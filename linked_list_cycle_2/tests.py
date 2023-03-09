import unittest

from linked_list_cycle_2.initial import Solution

from Utils.ListNode import ListNode

class TestDetectCycle(unittest.TestCase):
    def __init__(self):
        self.sol = Solution()

    
    def test_no_cycle(self):
        # Test a linked list with no cycle
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        self.assertEqual(self.sol.detect_cycle(head), None)
        
    def test_cycle(self):
        # Test a linked list with a cycle
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node2
        self.assertEqual(self.sol.detect_cycle(head), node2)
        
if __name__ == '__main__':
    unittest.main()
