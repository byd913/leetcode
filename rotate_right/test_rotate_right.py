import unittest

from rotate_right import Solution, ListNode

class TestRotateRight(unittest.TestCase):
    def node_list_equal(self, head1, head2):
        while head1 is not None and head2 is not None:
            self.assertEqual(head1.val, head2.val)
            head1 = head1.next
            head2 = head2.next
        
        self.assertIsNone(head1)
        self.assertIsNone(head2)

    def test_case1(self):
        solution = Solution()
        head = ListNode(1)
        cur = head
        for i in range(2, 6):
            node = ListNode(i)
            cur.next = node
            cur = node

        expect_list = [ListNode(4), ListNode(5), ListNode(1), ListNode(2), ListNode(3)]
        for i in range(0, len(expect_list)-1):
            expect_list[i].next = expect_list[i+1]
        result = solution.rotateRight(head=head, k=2)
        self.node_list_equal(result, expect_list[0])
            

    def test_case2(self):
        solution = Solution()
        head = ListNode(1)
        cur = head
        for i in range(2, 6):
            node = ListNode(i)
            cur.next = node
            cur = node

        expect_list = [ListNode(5), ListNode(1), ListNode(2), ListNode(3), ListNode(4)]
        for i in range(0, len(expect_list)-1):
            expect_list[i].next = expect_list[i+1]
        result = solution.rotateRight(head=head, k=1)
        self.node_list_equal(result, expect_list[0])

    def test_case3(self):
        solution = Solution()
        head = ListNode(0)
        cur = head
        for i in range(1, 3):
            node = ListNode(i)
            cur.next = node
            cur = node

        expect_list = [ListNode(2), ListNode(0), ListNode(1)]
        for i in range(0, len(expect_list)-1):
            expect_list[i].next = expect_list[i+1]
        result = solution.rotateRight(head=head, k=4)
        self.node_list_equal(result, expect_list[0])
    
    def test_case4(self):
        solution = Solution()
        head = None
        result = solution.rotateRight(head=head, k=4)
        self.node_list_equal(result, None)
        
    def test_case5(self):
        solution = Solution()
        head = ListNode(1)
        result = solution.rotateRight(head=head, k=4)
        self.node_list_equal(result, ListNode(1))
            

if __name__ == "__main__":
    unittest.main()
