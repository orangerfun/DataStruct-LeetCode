"""
建立一颗二叉树，中序遍历、前序遍历、后序遍历
"""

# 使用链表构建树
class Creat_Tree:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

# 中序遍历
def inorder(root):
	if root != None:
		inorder(root.left)
		print(root.data, end="\t")
		inorder(root.right)

# 前序遍历
def preorder(root):
	if root != None:
		print(root.data, end="\t")
		preorder(root.left)
		preorder(root.right)

# 后序遍历
def postorder(root):
	if root != None:
		postorder(root.left)
		postorder(root.right)
		print(root.data, end="\t")

# 构建二叉树
def Btree(root,val):
	newnode = Creat_Tree(val)
	if root == None:
		root = newnode
		return root
	else:
		current = root
		while current != None:
			backward = current
			if val < current.data:
				current = current.left
			else:
				current = current.right
		if val < backward.data:
			backward.left = newnode
		else:
			backward.right = newnode
		return root

if __name__ == "__main__":
	root = None
	data = [7,4,1,5,16,8,11,12,15,9,2]
	for val in data:
		root = Btree(root, val)
	print("中序遍历结果为：")
	inorder(root)
	print("\n前序遍历结果为：")
	preorder(root)
	print("\n后序遍历结果为：")
	postorder(root)







