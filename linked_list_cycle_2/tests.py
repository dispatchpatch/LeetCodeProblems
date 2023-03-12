import signal
from typing import List, Optional
import unittest


from linked_list_cycle_2.solution import Solution
from utilities.ListNode import ListNode


class TestDetectCycleInitial(unittest.TestCase):
    def test_no_cycle(self):
        # Test a linked list with no cycle
        head, cycle_node = build_node_list([1,2, 3, 4, 5], -1)
        self.assertEqual(Solution.detect_cycle_first_attempt(head), cycle_node)

    def test_cycle(self):
        # Test a linked list with a cycle
        head, cycle_node = build_node_list([1, 2, 3, 4, 5], 1)
        self.assertEqual(Solution.detect_cycle_first_attempt(head), cycle_node)

    def test_cycle_same_val(self):
        # This test denotes a fail in the initial solution
        head, cycle_node = build_node_list([-1,-7,7,-4,19,6,-9,-5,-2,-5], 6)
        self.assertNotEqual(Solution.detect_cycle_first_attempt(head), cycle_node)

class TestDetectCycleImproved(unittest.TestCase):
    def setUp(self) -> None:
        # Adding 5 second timeout to mimic LeetCode
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(5)
    
    def handle_timeout(self, signum, frame):
        raise TimeoutError("Test Exceeded TimeLimit")

    def test_no_cycle(self):
        # Test a linked list with no cycle
        head, cycle_node = build_node_list([1,2, 3, 4, 5], -1)
        self.assertEqual(Solution.detect_cycle_improved(head), cycle_node)

    def test_cycle(self):
        # Test a linked list with a cycle
        head, cycle_node = build_node_list([1, 2, 3, 4, 5], 1)
        self.assertEqual(Solution.detect_cycle_improved(head), cycle_node)

    def test_cycle_same_val(self):
        # This test succeeds where the initial solution failed
        head, cycle_node = build_node_list([-1,-7,7,-4,19,6,-9,-5,-2,-5], 6)
        self.assertEqual(Solution.detect_cycle_improved(head), cycle_node)

class TestDetectCycleTwoPointer(unittest.TestCase):
    def setUp(self) -> None:
        # Adding 5 second timeout to mimic LeetCode
        # signal.signal(signal.SIGALRM, self.handle_timeout)
        # signal.alarm(5)
        print("none")
    
    def handle_timeout(self, signum, frame):
        raise TimeoutError("Test Exceeded TimeLimit")

    def test_no_cycle(self):
        # Test a linked list with no cycle
        head, cycle_node = build_node_list([1,2, 3, 4, 5], -1)
        self.assertEqual(Solution.detect_cycle_two_point(head), cycle_node)

    def test_cycle(self):
        # Test a linked list with a cycle
        head, cycle_node = build_node_list([1, 2, 3, 4, 5], 1)
        self.assertEqual(Solution.detect_cycle_two_point(head), cycle_node)

    def test_cycle_same_val(self):
        # This test succeeds where the initial solution failed
        head, cycle_node = build_node_list([-1,-7,7,-4,19,6,-9,-5,-2,-5], 6)
        self.assertEqual(Solution.detect_cycle_two_point(head), cycle_node)


def build_node_list(vals: List[int], cycle_point: int) -> tuple[Optional[ListNode], Optional[ListNode]]:
    curr = None
    prev = None
    cycle_node = None
    head = None

    for i in range(len(vals)):
        curr = ListNode(vals[i])
        if not head:
            head = curr
        if prev:
            prev.next = curr
        prev = curr
        if i == cycle_point:
            cycle_node = curr
    
    if cycle_node:
        curr.next = cycle_node
    
    return (head, cycle_node)



if __name__ == '__main__':
    unittest.main()
