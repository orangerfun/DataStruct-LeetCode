def climb(i, n):
	m = [0 for _ in range(n+1)]
	m[1] = 1
	m[2] = 2
	for i in range(3, n+1):
		m[i] = m[i-1] + m[i-2]
	return m[n]


print(climb(0, 37))

# 1,2,3,5,8,13,21
