# Introduction
部分README.md文件中使用了网络上图片以及引用了一些博客内容，如若侵权联系**orangerfun@gmail.com**删图；
# Classification
* 递归:  `64.最短路径`  `70.爬楼梯`  `21. 合并两个有序链表`
* 动态规划： `64.最短路径`   `最长公共子串`  `最长公共子序列`   `最长回文子串`  `70.爬楼梯` `10.正则表达式匹配`
* 回溯剪枝
# 数据结构总结
## 1.树
### 二叉树构建
构建原则：左子树<树根<右子树<br>
**（1）一维数组表示二叉树**
* 左子树的索引是父节点索引值*2
* 右子树索引值是父节点索引值*2+1
```python3
#用一维数组建立一棵二叉查找树
def BTree_creat(btree, data, length):
"""
args:
  btree: list ,用于存储二叉树，初始化为[0]*C
  data: list, 原始数据
  length： len(data)
  注意btree的设置长度
"""
  for i in range(length):
    level = 1
    while btree[level] != 0:
      if btree[level] > data[i]:
        level = 2*level
      else:
        level = 2*level+1
    btree[level]=data[i]
```
**(2)链表表示二叉树**
```python3
# 使用链表构建树
class Creat_Tree:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

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
```
### 二叉树遍历
**（1）中序遍历：左子树-->树根-->右子树**
```python3
def inorder(root):
	if root != None:
		inorder(root.left)
		print(root.data, end="\t")
		inorder(root.right)
 ```
 **（2）前序遍历：树根-->左子树-->右子树**
 ```python3
 def preorder(root):
	if root != None:
		print(root.data, end="\t")
		preorder(root.left)
		preorder(root.right)
 ```
**（3）后序遍历：左子树-->右子树-->树根**
```python3
def postorder(root):
	if root != None:
		postorder(root.left)
		postorder(root.right)
		print(root.data, end="\t")
```
### 二叉树查找、删除、插入节点
**(1)查找**
```python3
def search(ptr, val):
	i = 1
	while True:
		if ptr.data == val:
			print("已找到，找了%d次"%i)
			return ptr
		elif ptr == None:
			return None
		elif ptr.data > val:
			ptr = ptr.left
		else:
			ptr = ptr.right
		i += 1
```
**(2)插入节点**
```python3
ptr = search(root, val)
if ptr != None:                 # 查找需要插入的节点
	print("该节点已经存在")
else:                           # 若不存在，将此节点建立到树中，Btree是上面提到的建立树的函数
	ptr = Btree(ptr, data)
```
# Thanks
感谢网络上一些博客提供思路



