# 拷贝此程序至LeetCode可直接运行

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 记录结果
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            temp = head
            # 入栈
            while count and temp:
                stack.append(temp)
                count -= 1
                temp = temp.next
            # 如果count不等于零，说明最后不满k个不需要转换
            if count:
                p.next = head
                break
            # count==0, 进行转换
            while stack:
                p.next = stack.pop()
                p = p.next
            # 将栈中的转换后连接上后面未转换内容
            p.next = temp
            # 更新head
            head = temp
        return dummy.next