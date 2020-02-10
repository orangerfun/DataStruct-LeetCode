class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 特殊情况
        if s == "" or len(s) == 1:
            return 0

        # 初始化矩阵
        dp = [0 for i in range(len(s))]
        if s[0]=="(" and s[1]==")":
            dp[1] = 2

        # 动态规划状态转移
        for i in range(2, len(s)):
            if s[i] == ")" and s[i-1]=="(":
                dp[i] = dp[i-2]+2
            elif s[i] == ")" and s[i-1] == ")":
                if s[i-dp[i-1]-1]=="(" and i-dp[i-1] > 0:
                    dp[i] = (dp[i-1] + 2 + dp[i-dp[i-1]-2]) if i-dp[i-1]-2 >=0 else (dp[i-1] + 2)
                    
        return max(dp)
        
solution = Solution()
x = "((())())(()))(()()("
print(solution.longestValidParentheses(x))