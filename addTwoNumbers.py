# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.toList(l1)
        l2 = self.toList(l2)
        l1.reverse()
        l2.reverse()
        l11 = "".join(str(x) for x in l1)
        l22 = "".join(str(x) for x in l2)
        l_sum = int(l11)+int(l22)
        res = [int(x) for x in str(l_sum)]
        l_sum_arr = ListNode(res[0])
        for i in range(len(res)):
                new_node = ListNode(res[i])
                new_node.next = l_sum_arr.next
                l_sum_arr.next = new_node
        l_sum_arr = l_sum_arr.next
        return l_sum_arr
                
    def toList(self, linked):
        arr = [ ]
        while(linked!=None):
          arr.append(linked.val)
          linked=linked.next
        return arr
                
        