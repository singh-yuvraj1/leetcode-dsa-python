# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Example 2:
# Input: head = [1,2]
# Output: [2,1]


# Example 3:
# Input: head = []
# Output: []
 

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


#brute force ---using extra array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        arr = []

        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        temp = head
        i = len(arr) - 1

        while temp:
            temp.val = arr[i]
            i -= 1
            temp = temp.next

        return head


if __name__ == "__main__":
    s = Solution()

    # Example 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head1 = s.reverseList(head1)

    while reversed_head1:
        print(reversed_head1.val, end=" ")
        reversed_head1 = reversed_head1.next
    print()      # 5 4 3 2 1

    # Example 2
    head2 = ListNode(1, ListNode(2))
    reversed_head2 = s.reverseList(head2)

    while reversed_head2:
        print(reversed_head2.val, end=" ")
        reversed_head2 = reversed_head2.next
    print()      # 2 1

    # Example 3
    head3 = None
    reversed_head3 = s.reverseList(head3)

    if not reversed_head3:
        print([])      # []

#time complexity: O(n) where n is the number of nodes in the linked list.
#space complexity: O(n) because we are using an extra array to store the values of the linked list nodes.


