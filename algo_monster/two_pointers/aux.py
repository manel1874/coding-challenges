class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list2node(linked_list: list[int]):
        if not linked_list:
            return None

        head = ListNode(val=linked_list[0])
        current_node = head
        for el in linked_list[1:]:
            current_node.next = ListNode(val=el)
            current_node = current_node.next

        return head