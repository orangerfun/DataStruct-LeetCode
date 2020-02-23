class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict

        def isCould(row, col, d):
            return not (d in rows[row] or d in cols[col] or d in boxes[boxindex(row, col)])
        
        def placeNum(row, col, d):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[boxindex(row, col)][d] += 1
            board[row][col] = str(d)
        
        def placeNextNum(row, col):
            
            if row == n-1 and col == n-1:
                nonlocal finished
                finished = True
            else:
                if col == n-1:
                    backtrack(row+1, 0)
                else:
                    backtrack(row, col+1)
        
        def removeNum(row, col, d):
            del rows[row][d]
            del cols[col][d]
            del boxes[boxindex(row,col)][d]
            board[row][col] = "."


        def backtrack(row, col):
            if board[row][col] == ".":
                for d in range(1,10):
                    if isCould(row, col, d):
                        placeNum(row, col, d)
                        placeNextNum(row, col)
                        # 当放下一个cell时遍历所有1-10的数字都不行时，进行回溯，修改当前位置的值
                        if not finished:
                            removeNum(row, col, d)
            else:
                placeNextNum(row, col)
        
        n = 9
        cols = [defaultdict(int) for i in range(n)]
        rows = [defaultdict(int) for i in range(n)]
        boxindex = lambda row, col: (row//3)*3+col//3
        boxes = [defaultdict(int) for i in range(n)]
        # 首先遍历所有cell，找出已经存在的数字，并初始化cols, rows, boxes, 便于后面判断某个数字是否存在
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    placeNum(i, j, d)
        finished = False
        backtrack(0, 0)