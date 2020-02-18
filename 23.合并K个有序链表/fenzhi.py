# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        interval = 1
        count = len(lists)

        # 特殊情况
        if count == 0:
            return None
        # 两两组合合并
        while interval<count:
            for i in range(0, count-interval, 2*interval):
                lists[i] = self.merge2list(lists[i], lists[i+interval])
            interval = 2*interval
        return lists[0]
    
    def merge2list(self, l1, l2):
        head=point=ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                point.next = l1
                l1 = l1.next
                point = point.next
            else:
                point.next = l2
                l2 = l2.next
                point = point.next
        if l1:
            point.next=l1
        else:
            point.next=l2
        return head.next

# 测试
lists = [ListNode(1), ListNode(2), ListNode(-1)]
solution = Solution()
result = solution.mergeKLists(lists)
while result != None:
    print(result.val)
    result=result.next
