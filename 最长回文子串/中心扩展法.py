def longestPaline(s):
	size = len(s)
	if size <= 1 :
		return s

	longestLine = []
	maxlength = 1
	for i in range(size):
		longestLine_odd, maxlength_odd = expand(s,i, i)
		longestLine_even, maxlength_even = expand(s,i,i+1)
		tempLine = longestLine_odd if maxlength_odd > maxlength_even else longestLine_even
		if len(tempLine) > maxlength:
			maxlength = len(tempLine)
			longestLine = tempLine
	return longestLine

def expand(s, left, right):
	while left >= 0 and right < len(s) and s[left] == s[right]:
		left = left - 1
		right = right + 1
	return s[left+1:right], right-left

if __name__ == '__main__':
	s = input("please input a string:")
	print(longestPaline(s))