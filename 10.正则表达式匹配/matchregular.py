class Solution:
    def isMatch(self, s, p):
        # 特殊情况处理
        if s==None or p==None:
            return False
        
        # dp矩阵初始化
        dp = [[False for j in range(len(p)+1)]for i in range(len(s)+1)]
        dp[0][0] = True
        for i in range(2,len(p)+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]

        # 动态规划
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1]==p[j-1] or p[j-1]==".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=="*":
                    if p[j-2]==s[i-1] or p[j-2]==".":
                        dp[i][j] = (dp[i][j-2] or dp[i-1][j-1] or dp[i-1][j])
                    else:
                        dp[i][j]=dp[i][j-2]
                        
        return dp[len(s)][len(p)]

if __name__=="__main__":
    s = "mississippi"
    p = "mis*is*p*."
    soulution = Solution()
    result = soulution.isMatch(s, p)
    print(result)