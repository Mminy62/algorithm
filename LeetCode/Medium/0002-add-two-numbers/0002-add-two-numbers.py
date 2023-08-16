# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         one, two = '', ''
#         while l1.next:
#             one += str(l1.val)
#             l1 = l1.next
#         one += str(l1.val)
#         one = one[::-1]

#         while l2.next:
#             two += str(l2.val)
#             l2 = l2.next
#         two += str(l2.val)
#         two = two[::-1]
        
#         result = str(int(one) + int(two))

#         headNode = ListNode(result[-1])
#         if len(result) > 1:
#             temp = headNode
#             for i in range(len(result)-2, -1, -1):
#                 temp.next = ListNode(result[i])
#                 temp = temp.next
    
#         return headNode

class Solution:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next