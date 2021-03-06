70.爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：

输入： 2

输出： 2

解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

来源：力扣（LeetCode）

链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
本问题其实常规解法可以分成多个子问题，爬第n阶楼梯的方法数量，等于 2 部分之和

爬上n−1 阶楼梯的方法数量。因为再爬1阶就能到第n阶

爬上n−2 阶楼梯的方法数量，因为再爬2阶就能到第n阶

所以我们得到公式 dp[n] = dp[n-1] + dp[n-2]
同时需要初始化 dp[0]=1 和 dp[1]=1

    class Solution:
    	def climbStairs(self, n: int) -> int:
        	if n < 3:
            	return n
        	a,b,temp = 1,2,0
        	for i in range(3, n + 1):
            	temp = a + b
            	a = b
            	b = temp
        	return temp

时间复杂度：O(n)

空间复杂度：O(1)