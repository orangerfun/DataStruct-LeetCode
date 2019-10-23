'''
动态规划求解最大公共子串
@author: orangerfun@gmail.com
'''
def maxstr(s1, s2, matrix):
	maxlength = 0
	#flag 用于求解子串
	flag = 0
	for i in range(len(s2)):
		for j in range(len(s1)):
			#如果在第一行（列），直接置1
			if s1[j] == s2[i] and (i==0 or j==0):
				m[i][j] = 1
			#在矩阵内部，状态转移
			elif s1[j] == s2[i] and (i!= 0 and j!=0):
				m[i][j] = m[i-1][j-1] + 1
			#记录最长的长度
			if m[i][j] > maxlength:
				maxlength = m[i][j]
				flag = i+1
	return s2[flag-maxlength:flag]

if __name__ == '__main__':
	s1 = "b"
	s2 = "bbcdghif"
	#构建矩阵记录最长子串
	m = [[0 for _ in range(len(s1))] for _ in range(len(s2))]
	print(maxstr(s1,s2,m))

