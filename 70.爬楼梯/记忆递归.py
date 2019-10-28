def climb(i, n, matrix):
	if i == n:
		return 1
	elif i > n:
		return 0
	elif m[i] != -1:
		return m[i]
	else:
		m[i] = climb(i+1, n, matrix) + climb(i+2, n, matrix)
	return m[i]
n = 7
m = [-1 for _ in range(n)]
print(climb(0, n, m))