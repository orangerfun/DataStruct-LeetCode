# 1.图的数据表示法：邻接矩阵法
# data里面每个列表存的是一个边的起点和终点

# data = [[1,2], [2,1], [1,5], [5,1], [2,3], [3,2], [2,4], [4,2], [3,4], [4,3]]
# arr = [[0]*6 for i in range(6)]
# for i in range(len(data)):
# 	tempi = data[i][0]
# 	tempj = data[i][1]
# 	arr[tempi][tempj] = 1
# for i in range(1, len(arr)):
# 	for j in range(1, len(arr[0])):
# 		print(arr[i][j], end=" ")
# 	print()


# 2. 图的数据表示法：邻接表法
class list_node:
	def __init__(self):
		self.val = 0
		self.next = None

data = [[1,2], [2,1], [1,5], [5,1], [2,3], [3,2], [2,4], [4,2], [3,4], [4,3]]
head = [list_node]*6
# 起点
for i in range(1, 6):
	head[i] = list_node()
	head[i].val = i
	head[i].next = None
	print("顶点%d=>"%i, end=" ")
	ptr = head[i]
	for j in range(len(data)):
		if data[j][0] == i:
			newnode = list_node()
			newnode.val = data[j][1]
			newnode.next = None
			ptr.next = newnode
			ptr = ptr.next
			print(ptr.val, end=" ")
	print()

