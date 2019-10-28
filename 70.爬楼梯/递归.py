def climb(i,n):
	if i == n:
		return 1
	elif i > n:
		return 0
	else:
		return climb(i+1, n)+climb(i+2, n)

print(climb(0,37))