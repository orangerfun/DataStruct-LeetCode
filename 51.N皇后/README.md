# 问题
皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击，即每个皇后都不在同一行，同一列，同一条斜线（主副对角线）上
# 解析
使用回溯法<br>
遍历每一行，从每一行中找符合条件的列；所谓的条件就是与已经存在的皇后不在同一行，同一列，同一条斜线上
* 用列表`col`记录已经存在的皇后所在列
* 用列表`master`记录已经存在的皇后的主对角线
* 用列表`slave`记录已经存在的皇后的副对角线<br>

**注意：** 同一条主对角线上的坐标`（i，j）` `i-j=常数`; 同一条副对角线上的元素坐标`(i,j)`  `i+j=常数`

因此判断条件如下：
```python
    for i in range(n):
      if i not in col and row+i not in master and row-i not in slave:
        col.append(i)
        master.append(row+i)
        slave.append(row-i)
```
其中row表示当前所在行，for循环遍历所有列，当找到合适列后将该元素的行列主副对角线放入对应的列表中，用于下次找下一个元素判断<br>
<br>
回溯<br>
当找到一个完整的结果(每一行都放置了皇后)或者无法继续放皇后时，需要回溯；即从上次的结果往后寻找

# 复杂度分析
**时间复杂度**
在第一行有N种选择，第二行有N-1种选择...第N行有1种选择，故时间复杂度`N!`<be>
    
**空间复杂度**
需要额外记录col, master, slave
空间复杂度为：`N`

```python
digui(col, master, slave, result)    # 递归结束就回溯
col.pop()
master.pop()
slave.pop()
```

程序见 `queen.py`
```python3
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
```

