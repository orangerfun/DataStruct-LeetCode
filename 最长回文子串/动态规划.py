def longestPalindrome(s):
	size = len(s)
	#当s只有1个或者0个（空）元素时，其本身就是回文串
	if size <= 1:
		return s

	maxlength = 1
	longestline = []

	m= [[False for _ in range(size)] for _ in range(size)]
	for r in range(1,size):
		for l in range(r):
			if s[r] == s[l] and (m[l+1][r-1] or r-l<=2):
				m[l][r] = True
				if r-l+1 >maxlength:
					maxlength = r-l+1
					longestline = s[l:r+1]
	return longestline

if __name__ == "__main__":
	s = input("please input a string:")
	print(longestPalindrome(s))

