class Solution:
    def solveNQueens(self, n):
        if n == 0:
            return []
        else:
            result = []     # 记录结果
            col = []        # 记录被用过的行
            master = []     # 记录主对角线
            slave = []      # 记录副对角线    
            self. digui(n, 0, col, master, slave,result)
            return result

    def digui(self, n, row, col, master, slave, result):
        # 递归结束，当所有行遍历结束后，将上一次结果保存道result
        if row == n:
            result.append(self.cal_result(col,n))
        # 遍历所有行
        for i in range(n):
            # 判断
            if i not in col and row+i not in master and row-i not in slave:
                col.append(i)
                master.append(row+i)
                slave.append(row-i)
                # 继续递归
                self.digui(n, row+1, col, master, slave,result)
                # 回溯
                col.pop()
                master.pop()
                slave.pop()
        return result

    # 利用记录的列来拼接结果
    def cal_result(self,col,n):
        return ["."*j+"Q"+"."*(n-j-1) for j in col]

solution = Solution()
print(solution.solveNQueens(5))