class Solution:
    def minPathSum(self, grid):
        # 动态规划算法
        # d[i][j]是坐标（i，j）位置到右下角位置的最短路径
        x, y = len(grid), len(grid[0])
        # 记录矩阵
        dp = [[0 for _ in range(y)] for i in range(x)]
        dp[x-1][y-1] = grid[x-1][y-1]

        for i in range(x-1,-1,-1):
            for j in range(y-1,-1,-1):
                if j == y-1 and i != x-1:
                    dp[i][j] = dp[i+1][j] + grid[i][j]
                elif i == x-1 and j != y-1:
                    dp[i][j] = dp[i][j+1] + grid[i][j]
                elif i != x-1 and j != y-1:
                    dp[i][j] = grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]

matrix = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
solution = Solution()
print(solution.minPathSum(matrix))
