# 使用深度优先遍历
class list_node:
	def __init__(self):
		self.val = 0
		self.next = None

data = [[1,2], [2,1], [1,3], [3,1], [2,4], [4,2], [2,5], [5,2],\
		[3,6], [6,3], [3,7], [7,3], [4,8], [8,4], [5,8], [8,5],\
		[6,8], [8,6], [8,7], [7,8]]

# 构建邻接表
head = [list_node]*9
for i in range(1, 9):
	head[i] = list_node()
	head[i].val = i
	head[i].next = None
	ptr = head[i]
	for j in range(len(data)):
		if data[j][0] == i:
			newnode = list_node()
			newnode.val = data[j][1]
			newnode.next = None
			ptr.next = newnode
			ptr = ptr.next

# 打印邻接表
print("图的邻接表内容为：")
for i in range(1, len(head)):
	ptr = head[i]
	while ptr != None:
		print(ptr.val, end=" ")
		ptr = ptr.next
	print()

# 深度遍历/递归
run = [0]*9
def dfs(current):
	run[current] = 1
	print(current, end=" ")
	ptr = head[current].next
	while ptr!=None:
		if run[ptr.val] == 0:
			dfs(ptr.val)
		ptr = ptr.next
print("深度优先遍历顶点:")
dfs(1)

