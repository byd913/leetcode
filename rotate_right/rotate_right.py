# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        link_length = 0
        cur = head
        tail = cur
        while cur != None:
            tail = cur
            link_length += 1
            cur =  cur.next
        if link_length == 0:
            return head
        
        k = k % link_length
        if  k == 0:
            return head

        break_node = head
        break_link_pos = link_length - k -1
        # print link_length

        for i in range(0, break_link_pos):
            break_node = break_node.next
        # print break_node.val
        
        tail.next = head
        new_head = break_node.next
        break_node.next = None
        return new_head
        

if __name__ == "__main__":
        head = ListNode(1)
        cur = head
        for i in range(2, 6):
            node = ListNode(i)
            cur.next = node
            cur = node

        solution = Solution()
        result = solution.rotateRight(head=head, k=1)
        
        while result is not None:
            print result.val
            result = result.next