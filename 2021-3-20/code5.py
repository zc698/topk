5.最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

#思路：
第1步：定义状态
dp[i][j] 表示子串 s[i..j] 是否为回文子串，这里子串 s[i..j] 定义为左闭右闭区间，可以取到 s[i] 和 s[j]。
第2步：思考状态转移方程
dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
边界条件是：表达式 [i + 1, j - 1] 不构成区间，即长度严格小于 2，即 j - 1 - (i + 1) + 1 < 2 ，整理得 j - i < 3。
在 s[i] == s[j] 成立和 j - i < 3 的前提下，直接可以下结论，dp[i][j] = true，否则才执行状态转移。
第3步：考虑初始化
初始化的时候，单个字符一定是回文串，因此把对角线先初始化为 true，即 dp[i][i] = true 。
第4步：考虑输出
只要一得到 dp[i][j] = true，就记录子串的长度和起始位置，没有必要截取，这是因为截取字符串也要消耗性能，记录此时的回文子串的「起始位置」和「回文长度」即可。


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start = 0
        max_len = 1
        dp = [[(False) for _ in range(n) ] for _ in range(n)]
        for i in range (n):
            dp[i][i] = True
        for j in range(1,n):
            for i in range(0,j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i +1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
        
        
时间复杂度：O(N^2)
空间复杂度：O(N^2)
