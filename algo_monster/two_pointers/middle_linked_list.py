"""Find the middle node of a linked list.

Input: 0 1 2 3 4

Output: 2

If the number of nodes is even, then return the second middle node.

Input: 0 1 2 3 4 5

Output: 3
"""

from aux import ListNode

class Solution:
    def middle_node(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return -1

        left = head
        right = head

        while right.next and right.next.next:
            left = left.next
            right = right.next.next

        if right.next:
            return left.next.val
        else:
            return left.val
        


if __name__ == "__main__":
    head = ListNode.list2node([0,1,2,3,4,5])
    sol = Solution().middle_node(head)
    print(sol)
