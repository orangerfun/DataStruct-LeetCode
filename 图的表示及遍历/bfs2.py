# 图的广度优先遍历
class node:
	def __init__(self, val):
		self.val = val
		self.next = None

data = [[1,2], [2,1], [1,3], [3,1], [2,4], [4,2], [2,5], [5,2],\
		[3,6], [6,3], [3,7], [7,3], [4,8], [8,4], [5,8], [8,5],\
		[6,8], [8,6], [8,7], [7,8]]

# 构建邻接表
head = [node]*9
for i in range(1, 9):
	head[i] = node(i)
	ptr = head[i]
	for j in range(len(data)):
		if data[j][0] == i:
			newnode = node(data[j][1])
			ptr.next = newnode
			ptr = ptr.next

# 广度优先
def bfs(current, nodes, run):
	nodes.append(current)
	while nodes:
		node = nodes.pop(0)
		if run[node] == 0:
			print(node, end=" ")
			run[node] = 1
			ptr = head[node].next
			while ptr != None:
				nodes.append(ptr.val)
				ptr = ptr.next

run = [0]*9
bfs(1, [], run)
