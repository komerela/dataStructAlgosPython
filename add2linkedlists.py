# You are given 2 non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of the nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807

l1 = 2, 4, 3
l2 = 5, 6, 4


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def linkedListStr(l):
        if l:
            return ''
        return str( l.val ) + '->' + linkedListStr(l.next )

        print


class Solution:

    def addTwoNumbers(self, l1, l2):

        print('')
        print('inside function...')

        # Declare pointers to iterate through both linked lists
        ptr1 = l1
        ptr2 = l2

        # declare current carry over incase the values in the lined lists go over one digit

        carry = 0

        # declare current variable to help traverse & add nodes to the new list
        # declare head variable to be head of the list

        head = ListNode(0)
        current = ListNode(0)

        # Iteration condition using while loop

        while ptr1 and ptr2 or carry:

            print(ptr1.val, ptr2.val, carry)

            # Determine current value and carry over

            currentVal = carry

            currentVal += 0 if ptr1 is None else ptr1.val
            currentVal += 0 if ptr2 is None else ptr2.val
           
            if currentVal >= 10:
                currentVal -= 10
                carry = 1
            else:
                carry = 0

            print(currentVal, carry)

            # add current value as it will always atleast be 1
            current.next = ListNode(currentVal)
            current = current.next

            # Add base cases for iterating LinkedLists

            if ptr1 is None and ptr2 is None:
                break
            elif ptr1 is None:
                ptr2 = ptr2.next
            elif ptr2 is None:
                ptr1 = pt1.next
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            return head.next


# Recursively print linkedlist


# create linkedlists
# 1st linked list
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(l1, l1.next, l1.next.next)

# 2nd linkedList

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


# Add Linked Lists
s = Solution()
print(s.addTwoNumbers(l1, l2))


# print( s.addTwoNumbers( l1, l2 ) )
