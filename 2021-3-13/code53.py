"""53.最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
动态规划的是首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 res
如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
每次比较 sum 和 res的大小，将最大值置为res，遍历结束返回结果
时间复杂度：O(n)
空间复杂度：O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sum = 0
        for i in range(len(nums)):
            if sum > 0 :
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(sum,res)
        return res
