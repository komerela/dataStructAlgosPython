# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

        1 -> 2 -> 4      1 -> 3 -> 4 -> 5 ->6
        l1                         l2

new_List 0 -> 1 ->
         (start new merged list)

1. set variables
"""


class ListNode:
    # constructor
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # A linked list class with a single head node


class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for linked list

    # Merge function for Linked list
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # set variables
        new_list = ListNode()  # used to manipulate the new merged list
        ans = new_list  # head of new merged list

        # create loop
        while l1 and l2:
            if l1.val <= l2.val:
                new_list.next = l1  # store the node in the new_list
                l1 = l1.next

            elif l2.val < l1.val:
                new_list.next = l2
                l2 = l2.next

            new_list = new_list.next

        if l1:
            new_list.next = l1

        elif l2:
            new_list.next = l2

        return ans.next


if __name__ == "__main__":
    l = ListNode(10)
    l2 = ListNode(8, l)

    o = ListNode(-1)
    n = ListNode(-3, o)

    s = LinkedList()
    res = s.mergeTwoLists(l2, n)

    while res:
        print(res.val)
        res = res.next
