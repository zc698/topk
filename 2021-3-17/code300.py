"""
300.最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

思路：
状态定义：

dp[i]的值代表 nums 前 i个数字的最长子序列长度。
转移方程： 设 j∈[0,i)，考虑每轮计算新 dp[i]时，遍历 [0,i)列表区间，做以下判断：

当 nums[i] > nums[j]时： nums[i]可以接在 nums[j]之后（此题要求严格递增），此情况下最长上升子序列长度为 dp[j] + 1；
当 nums[i] <= nums[j]时： nums[i]无法接在 nums[j]之后，此情况上升子序列不成立，跳过。
上述所有 1. 情况 下计算出的 dp[j] + 1dp[j]+1 的最大值，为直到i 的最长上升子序列长度（即 dp[i]）。实现方式为遍历j 时，每轮执行 dp[i] = max(dp[i], dp[j] + 1)。
转移方程： dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)。
初始状态：
dp[i]所有元素置1，含义是每个元素都至少可以单独成为子序列，此时长度都为1。
返回值：
返回 dp列表最大值，即可得到全局最长上升子序列长度。


"""



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
        
"""
时间复杂度：O(n^2),其中n为数组nums的长度。
空间复杂度:O(n)，需要额外使用长度为n的dp数组。
"""

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


时间复杂度：O(nlogn)。数组nums 的长度为n，我们依次用数组中的元素去更新d数组，而更新d数组时需要进行O(logn) 的二分搜索，所以总时间复杂度为 O(nlogn)。
空间复杂度：O(n)，需要额外使用长度为n 的d 数组。
"""
