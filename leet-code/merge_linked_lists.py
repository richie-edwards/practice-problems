"""
LeetCode 21 Merge Two Sorted Lists
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return

        if not l1 and l2:
            return l2

        if not l2 and l1:
            return l1

        if l1.val <= l2.val:
            result = l1
            l1 = l1.next
        else:
            result = l2
            l2 = l2.next

        tail = result

        while l1 or l2:
            if l1 is None or (l2 and l2.val <= l1.val):
                tail.next = l2
                tail = tail.next
                l2 = l2.next
            else:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
        return result

    def print_list_node(self, list_node):
        result = []
        while list_node:
            result.append(list_node.val)
            list_node = list_node.next
        print(result)


# l1 = ListNode(3)
# l1.next = ListNode(5)
# l1.next.next = ListNode(6)
# l2 = ListNode(2)
# l2.next = ListNode(3)
# l2.next.next = ListNode(7)
# l2.next.next.next = ListNode(8)

l1 = ListNode(3)
l2 = None

# l1 = ListNode(-9)
# l1.next = ListNode(3)
# l2 = ListNode(5)
# l2.next = ListNode(7)

test = Solution()
test.print_list_node(test.mergeTwoLists(l1, l2))
