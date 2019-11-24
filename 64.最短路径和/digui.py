class Solution:
    # 递归算法，超时
    def minPathSum(self, grid):
        i,j = 0, 0
        return self.digui(i,j,grid)

    def digui(self,i,j,grid):
        if i == len(grid)-1:
            return sum(grid[i][j:])
        elif j == len(grid[0])-1:
            return sum([grid[k][j] for k in range(i, len(grid))]) 
        else:
            result = min(self.digui(i+1,j,grid), self.digui(i,j+1,grid)) + grid[i][j]
        return result

matrix = [
  [1,3,1],
  [1,5,1],
  [4,2,1]]
solution = Solution()
print(solution.minPathSum(matrix))