# 拷贝此程序至Leetcode,可以直接运行

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 递归算法，尾递归，从尾部开始转换
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                temp = head.next
                head.next = cur
                cur = head
                head = temp
                count -= 1
            head = cur
        return head