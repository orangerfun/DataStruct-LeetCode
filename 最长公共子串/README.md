# 题目说明
求两个字符串中最长连续相同的子串长度
#### 例1：
    str1=“1AB2345CD”,str2=”12345EF”,则str1，str2的最长公共子串为2345
#### 例2：
    A = "hellowworld"   B="loop",  则A和B的最长公共子串是“lo”
# 动态规划法
**定义：** res[i][j]是以A[i]和B[j]为最后一个元素的最长公共子串的长度,以例2为例，构建如下表格：<br>
![](http://www.github.com/orangerfun/LeetCode/raw/master/最长公共子串/0.png)
所以递推公式为：

    当 i=0 或 j=0，res[i][j] = 0
    当 A[i] = B[j]时，res[i][j] = res[i-1][j-1]+1
    当 A[i] != B[j]时，res[i][j] = 0
    
