def longestString(s1,s2):
	m = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
	flag = 0
	maxlength = 0
	for i in range(1,len(s2)+1):
		for j in range(1,len(s1)+1):
			if s1[j-1] == s2[i-1]:
				m[i][j] = m[i-1][j-1]+1
				if maxlength < m[i][j]:
					maxlength = m[i][j]
					flag = i
			else:
				m[i][j] = 0
	return maxlength, s2[i-maxlength:i]

if __name__ == '__main__':
	string1 = input("please input a string:")
	string2 = input("please input another string:")
	print(longestString(string1,string2))
