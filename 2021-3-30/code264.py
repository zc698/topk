264.丑数
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

日期：2021.3.30

思路：
预计算 1690 个丑数：
初始化数组 nums 和三个指针 i2，i3，i5 。
循环计算所有丑数。每一步：
在 nums[i2] * 2，nums[i3] * 3 和 nums[i5] * 5 选出最小的数字添加到数组 nums 中。
将该数字对应的因子指针向前移动一步。
在数组中返回所需的丑数。

时间复杂度：O(1),时间检索答案和大约1690×5=8450 次的预计算操作。
空间复杂度：常数空间用保存 1690 个丑数。


class Ugly:
    def __init__(self):
        self.nums = nums = [1,]
        i2 = i3 = i5 = 0
        for i in range(1,1690):
            ugly = min(nums[i2] * 2,nums[i3] * 3,nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1


class Solution:
    ugly = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.ugly.nums[n - 1]
