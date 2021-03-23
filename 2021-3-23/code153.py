153.寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
请找出其中最小的元素。
输入：nums = [3,4,5,1,2]
输出：1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
二分法
1.找到数组的中间元素 mid。
2.如果中间元素 > 数组第一个元素，我们需要在 mid 右边搜索变化点。
3.如果中间元素 < 数组第一个元素，我们需要在 mid 左边搜索变化点。
4.当我们找到变化点时停止搜索，当以下条件满足任意一个即可：
nums[mid] > nums[mid + 1]，因此 mid+1 是最小值。
nums[mid - 1] > nums[mid]，因此 mid 是最小值。


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 0,n-1
        if nums[right] > nums[0] or n == 1:
            return nums[0]
        while right >= left:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1






时间复杂度：O(logN)
空间复杂度：O(1)
