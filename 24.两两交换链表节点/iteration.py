# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 使用迭代来解决
    def swapPairs(self, head: ListNode) -> ListNode:
        ptr = head
        res = ListNode(0)
        head = res
        while ptr != None and ptr.next != None:
            res.next=self.exchange(ptr)
            res = res.next.next
            ptr = ptr.next
        if ptr != None:
            res.next = ptr
        return head.next
     
    def exchange(self, ptr):
        first = ptr
        second = ptr.next
        first.next = second.next
        second.next = first
        return second

if __name__ == "__main__":
    zero = ListNode(0)
    one = ListNode(1)
    two = ListNode(2)
    zero.next = one
    one.next = two
    

    solution = Solution()
    result = solution.swapPairs(zero)

    while result != None:
        print(result.val, end=" ")
        result=result.next
        