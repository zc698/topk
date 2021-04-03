470.用 Rand7() 实现 Rand10()

已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。

示例 1:

输入: 1

输出: [7]

来源：力扣（LeetCode）

链接：https://leetcode-cn.com/problems/implement-rand10-using-rand7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：(rand7() - 1) * 7 + rand7()
首先rand7() - 1 得到的数的集合为{0,1,2,3,4,5,6}；
再乘7后得到的集合A为{0,7,14,21,28,35,42}
后面rand7()得到的集合B为{1,2,3,4,5,6,7}

    class Solution:
		def rand10(self):
			while 1:
				num = (rand7() - 1) * 7 + rand7()
				if num <= 40:
					return 1 + num % 10

时间复杂度：期望时间复杂度为O(1),但最坏情况下会达到O(∞)（一直被拒绝）。

空间复杂度：O(1)