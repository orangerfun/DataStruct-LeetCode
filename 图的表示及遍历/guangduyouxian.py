#图的广度优先遍历


# 队列最大容量
MaxSize = 10
front = -1
rear = -1


class Node:
	def __init__(self, x):
		self.x = x
		self.next = None


# 构建邻接表
class GranphLink:
	def __init__(self):
		self.first = None    # 记录表头
		self.last = None	 # 记录表尾位置

	# 打印表
	def my_print(self):
		current = self.first
		while current != None:
			print(current.x, end=" ")
			current = current.next
		print()

	# 在表尾加入节点
	def insert(self, x):
		newnode = Node(x)
		if self.first == None:
			self.first = newnode
			self.last = newnode
		else:
			self.last.next = newnode
			self.last = self.last.next


# 队列数据存入
def enqueue(value):
	global MaxSize
	global rear
	global queue
	if rear>=MaxSize:
		return
	rear += 1
	queue[rear]=value


# 队列数据取出
def dequeue():
	global front
	global queue
	if front == rear:
		return -1
	front += 1
	return queue[front]


def bfs(current):
	global front
	global rear
	global Head
	global run
	enqueue(current)   # 将第一个数加入队列
	run[current] = 1   # 遍历过的数做上标记
	print(current, end=" ")
	while front!=rear:
		current = dequeue()
		tempNode = Head[current].first
		while tempNode != None:
			if run[tempNode.x] == 0:
				enqueue(tempNode.x)
				run[tempNode.x] = 1
				print(tempNode.x, end=" ")
			tempNode = tempNode.next

data = [[1,2], [2,1], [1,3], [3,1], [2,4], [4,2], [2,5], [5,2],\
		[3,6], [6,3], [3,7], [7,3], [4,8], [8,4], [5,8], [8,5],\
		[6,8], [8,6], [8,7], [7,8]]

run = [0]*9
queue = [0]*MaxSize
Head = [GranphLink]*9

print("图的邻接表内容:")
for i in range(1, 9):
	print(i, end=" ")
	Head[i] = GranphLink()
	for j in range(len(data)):
		if data[j][0] == i:
			dataNum = data[j][1]
			Head[i].insert(dataNum)
	Head[i].my_print()

print("广度优先遍历节点:")
bfs(1)
print()