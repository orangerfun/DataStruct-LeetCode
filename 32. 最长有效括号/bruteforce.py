# 暴力法
class Solution:
    def longestValidParentheses(self, s: str):
        maxlen = 0
        # 每次取长度为偶数的子字符串来判断是否有效，并更新最大长度
        for i in range(len(s)):
            for j in range(i+2, len(s)+1, 2):
                string = s[i:j]
                if self.isValid(string):
                    maxlen = max(maxlen, len(string))
        return maxlen
                    
    # 判断一个子字符串是否有效
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")" and len(stack)>0:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        else:
            return True

solution = Solution()
x = "((())())(()))(()()("
print(solution.longestValidParentheses(x))