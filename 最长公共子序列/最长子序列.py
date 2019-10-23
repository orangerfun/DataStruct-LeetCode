'''
使用动态规划实现最长子序列求解
@author: orangerfun@gmail.com
'''

def LCS(s1, s2):
	#定义两个矩阵，一个用于计算最长子序列；一个用于最后回溯求解最长子序列（记录方向）
	m = [[0 for _ in range(len(s1)+1)] for j in range(len(s2)+1)]
	flag = [["q" for _ in range(len(s1)+1)] for j in range(len(s2)+1)]

	for i in range(len(s2)):
		for j in range(len(s1)):
			if s1[j] == s2[i]:
				m[i+1][j+1] = m[i][j] + 1
				flag[i+1][j+1] = "done"

			elif s1[j] != s2[i] and (m[i][j+1]>m[i+1][j]):
				m[i+1][j+1] = m[i][j+1]
				flag[i+1][j+1] = "up"

			elif s1[j] != s2[i] and (m[i][j+1] <= m[i+1][j]):
				m[i+1][j+1] = m[i+1][j]
				flag[i+1][j+1] = "left"
	# print(m)
	# print(flag)

	i, j = len(s2), len(s1)
	result = []
	while m[i][j]:
		if flag[i][j] == "done":
			result.append(s1[j-1])
			i -= 1
			j -= 1

		elif flag[i][j] == "left":
			j -= 1

		elif flag[i][j] == "up":
			i -= 1
	result.reverse()
	return "".join(result)

if __name__ == '__main__':
	s1 = "123456778"
	s2 = "357486782"
	print("result:",LCS(s1, s2))


