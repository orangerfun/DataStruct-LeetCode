# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 递归解决
    def swapPairs(self, head: ListNode) -> ListNode:
    	# 递归结束条件
        if head == None or head.next == None:
            return head
        
        first = head
        second = head.next

        # 递归
        first.next = self.swapPairs(second.next)
        second.next = first
        return second

# 测试
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
        