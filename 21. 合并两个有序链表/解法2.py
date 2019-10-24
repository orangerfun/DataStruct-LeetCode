class ListNode():
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):
	def merge(self, l1, l2):
		if l1 == None:
			return l2
		elif l2 == None:
			return l1
		elif l1.val < l2.val:
			l1.next = self.merge(l1.next, l2)
			return l1
		else:
			l2.next = self.merge(l1,l2.next)
			return l2

l1 = [1,4,6]
l2 = [2,3,9,10]
node1, node2 = ListNode(l1[0]), ListNode(l2[0])
ptr1,ptr2 = node1, node2
for i in range(1,len(l1)):
	node1.next = ListNode(l1[i])
	node1 = node1.next
for j in range(1,len(l2)):
	node2.next = ListNode(l2[j])
	node2 = node2.next

solution = Solution()
l3 = solution.merge(ptr1,ptr2)
while l3 != None:
	print(l3.val, end = " ")
	l3 = l3.next




	
		
		